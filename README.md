# sandboxプロジェクト

## 概要

Pythonが正しくインストールされていることを確認し，
ディレクトリ構成のサンプルのために作成されたプロジェクトです．

## 使い方 (Linux OS)

Python 3.x および venv をインストールしてください．    
`python3` コマンドで Python 3.x のインタプリタが起動するようにしてください．

例えば，Ubuntu 20.04.5 LTS の場合は以下のコマンドを実行することで，インストールができます．
```
$ sudo apt install python3 python3.8-venv -y
```

以下の手順で環境構築とテスト実行ができます．
処理の詳細は `scripts/makeenv.sh`, `Makefile`を参照してください．

```
$ make
```

以下のコマンドでサンプルプログラムを実行できます．
行列積演算のサンプルプログラムの結果が出力されます．

```
$ make run
```

テストは以下のコマンドで実行できます．

```
$ make test
```

以下のコマンドで作成した環境を削除できます．

```
$ make clean
```

## インストール (Windows)

`python' コマンドで Python 3.x のインタプリタが起動するようにしてください．    
必要に応じて，パスの設定を修正してください．

以下の手順で環境構築とテスト実行ができます．
処理の詳細は `scripts\\makeenv.bat`, `make.bat`を参照してください．

```
> make
```

(Windows PowerShell の場合は `.\make.bat`)

以下のコマンドでサンプルプログラムを実行できます．
行列積演算のサンプルプログラムの結果が出力されます．

```
> make run
```

(Windows PowerShell の場合は `.\make.bat run`)

テストは以下のコマンドで実行できます．

```
> make test
```

(Windows PowerShell の場合は `.\make.bat test`)

以下のコマンドで作成した環境を削除できます．

```
> make clean
```

(Windows PowerShell の場合は `.\make.bat clean`)
