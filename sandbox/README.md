# sandboxプロジェクト

## 概要

Pythonが正しくインストールされていることを確認し，
ディレクトリ構成のサンプルのために作成されたプロジェクトです．

## インストール

以下の手順でインストールできます．
処理の詳細は`makeenv.sh`, `Makefile`を参照してください．

```
$ source makeenv.sh
$ source activate
$ make
```

## 使い方

以下のコマンドでサンプルプログラムを実行できます．
行列積演算のサンプルプログラムの結果が出力されます．

```
$ python sandbox/sample.py
```

テストは以下のコマンドで実行できる．   
`make test` でもよい．

```
$ python -m unittest tests/test_sample.py
```
