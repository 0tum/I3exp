import sys
import os
import time
import scipy.io.wavfile as wav
import numpy as np


def visualize_wav(audio, sample_rate):
    # フーリエ変換を行う
    fft_data = np.fft.fft(audio)

    # 振幅スペクトルを計算 (絶対値を取る)
    amp_spec = np.abs(fft_data)

    # 正の周波数成分のみを取り出す
    N = len(fft_data)
    freq = np.fft.fftfreq(N, d=1.0/sample_rate)
    positive_freq = freq[freq >= 0]
    positive_amp_spec = amp_spec[:len(positive_freq)]

    # 最大振幅を求める
    max_amp = np.max(positive_amp_spec)

    # 出力する文字列を作成
    output = "Visualizer:\n"
    bin_width = 500
    num_bins = int(np.ceil(positive_freq[-1] / bin_width))

    for i in range(num_bins):
        bin_start = i * bin_width
        bin_end = (i + 1) * bin_width
        bin_freq = bin_start + (bin_end - bin_start) / 2
        bin_amps = positive_amp_spec[(
            positive_freq >= bin_start) & (positive_freq < bin_end)]
        bin_max_amp = np.max(bin_amps) if bin_amps.size > 0 else 0
        # バーの高さにメリハリをつけるために7乗している
        bar_length = int((bin_max_amp / max_amp)**7 * 50)
        output += f'{"|" * bar_length}\n'

    clear_console()
    print(output)


def clear_console():
    # コンソールをクリアする
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 visualize.py <sound_file_name>.wav")
        sys.exit(1)

    sound_name = sys.argv[1]

    # wavファイルを読み込む
    sample_rate, audio_data = wav.read(sound_name)

    # 音声データの長さを秒単位で計算する
    duration_seconds = len(audio_data) / sample_rate

    # 音声データを分割する数
    split = int(duration_seconds * 10)

    segment_length = len(audio_data) // split

    start_time = time.time()

    # スペクトル強度を表示
    for i in range(split):
        elapsed_time = time.time() - start_time
        expected_time = i * 0.1

        # 時間調整のためにスリープ
        if expected_time > elapsed_time:
            time.sleep(expected_time - elapsed_time)

        # 区間を切り出す
        start = i * segment_length
        # 範囲をチェックして超えないようにする
        end = min(start + segment_length, len(audio_data))
        segment = audio_data[start:end]
        visualize_wav(segment, sample_rate)


if __name__ == "__main__":
    main()
