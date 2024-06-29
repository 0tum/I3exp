# 音楽ビジュアライザー
![alt](https://macsoft.jp/wp-content/uploads/2022/02/My-Music-Visualizer-2_ss-1024x570.jpg)
イメージ画像

## 概要
周波数ごとのスペクトルで振幅を表示してwavファイルを可視化します。

##　使い方
```
visualize.sh hogehoge.wav
```
とターミナルに入力すると使えます。同梱のdoremi.wavやdq1.wavをまずは試してみてください。

## 仕組み（実装）
フーリエ変換を音楽に適用すると音楽の周波数スペクトルを得ることができます。

wavファイルを一定の長さで分割し、それぞれに対してフーリエ変換を施します。
