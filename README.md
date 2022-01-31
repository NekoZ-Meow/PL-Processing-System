# welcome Project Hiyo
プログラミング言語 長期課題2「言語処理系の開発」
ここには2021年度秋学期情報理工学部専門科目プログラミング言語長期課題2の全てがまとめられています。

## 成果物の在処とドキュメント群について
ドキュメントは Document/index.html を開き、Webページ形式で閲覧できます。
全ての成果物は https://github.com/NekoZ-Meow/PL-Processing-System に保管されています。
設計図はドキュメントから確認することができますが、vm_design フォルダに入っているastahファイルや、vm_design/svg 内のsvgファイルから直接見ることもできます。

## 言語仕様について
言語仕様については bnf/('8'*).ebnf にEBNFが入っています。
bnf/diagrams に構文図式が入っています。構文図式をすべてまとめたものや、EBNMFと構文図式のまとめの図、細かく分類されたものまで様々な形式で入っています。構文図式はRailroad Diagram Generator (https://www.bottlecaps.de/rr/ui) で作成しています。

## parserについて
この言語を定義し、yaccとlexを用いて構文解析をするparserは parser フォルダにあり、make test で木構造を出力することができます。コンパイルしてできたファイル群をもとに戻す時は make clean で実行できます。make testで解析されるソースコードはsrc.txtです。

## 仮想マシンについて
仮想マシンのpythonによるソースコードは hiyo フォルダに入っています。PL-Processing-Systemで make を使ってビルドできます。詳しくはドキュメントのマニュアルをご覧ください。 make clean でダウンロードした初期の状態に戻せます。

## アプリケーションについて
アプリケーションを起動するには make prepare を行う必要があります。詳しくはドキュメントの「マニュアル」をご覧ください。

## テストケースについて
test_txt フォルダにテストケース群が入っています。これらはテストのために使用しました。詳しくはドキュメントの「テスト」をご覧ください。実際に行われたテストのソースコードはtest_txt フォルダの中身を見ることで確認できます。また、テストを実行するには make test-files で行えます。

## make コマンドについて
- `make all`

    - lex、yaccを使用して構文解析器を生成したのち、プロジェクトのディレクトリにコピーします。

- `make test`

    - ('8'*)のインタラクティブシェルを起動します。

- `make open`

    - アプリケーション('8'*)を実行します。

- `make test-files`

    - テスト用ソースプログラムを('8'*)で実行します。

- `make install`

    - アプリケーションに('8'*)をインストールします。

- `make lint`

    - pylintを実行します。

- `make clean`

    - `__pycache__`などの一時的に生成されるファイルを削除します。

- `make doc`
    
    - pydocを実行し、ターミナル上で表示します。

- `make pydoc`

    - pydocを実行し、ブラウザ上で表示します。

- `make prepare`

    - ('8'*)の実行に必要なパッケージをインストールします。


## CopyRight
2022 Project Hiyo