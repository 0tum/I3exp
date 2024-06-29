# 音楽ビジュアライザー
![alt](https://macsoft.jp/wp-content/uploads/2022/02/My-Music-Visualizer-2_ss-1024x570.jpg)
イメージ画像(https://macsoft.jp/my-music-visualizer/)

## 概要
周波数ごとの振幅をターミナル上で表示してwavファイルを可視化します。

## 使い方
```
visualize.sh hogehoge.wav
```
とターミナルに入力すると使えます。
どういう動きをするのかは実際に使ってみるとすぐわかるはずなので，同梱のdoremi.wavやdq1.wavをまずは試してみてください。

## 仕組み（実装）
フーリエ変換を音楽に適用すると音楽の周波数スペクトルを得ることができます。
このプログラムはwavファイルを細かく分割してそれぞれ周波数スペクトルに変換し，周波数バンド(デフォルトだと500Hz)ごとの振幅をリアルタイムに表示します．



