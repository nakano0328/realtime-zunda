# realtime-zunda

ずんだもんとリアルタイムで話せるコードです

## 概要

このプロジェクトは、音声認識とAI音声合成を組み合わせて、ずんだもんのキャラクターとリアルタイムで会話できるPythonアプリケーションです。

## まとめ記事

このスクリプトの詳細や利用方法に関して、以下のまとめ記事をご覧ください。

- [Zennの記事](https://zenn.dev/hibari_inc/articles/realtime-zunda)
- [Qiitaの記事](https://qiita.com/nakano0328/items/2c4542fc97417f9e015d)

### 主な機能

- **音声認識**: マイクからの音声入力をテキストに変換
- **AI会話**: Google Gemini APIを使用してずんだもんの性格で応答生成
- **音声合成**: VOICEVOXを使用してずんだもんの声で音声出力
- **リアルタイム会話**: 連続的な会話セッション

### ファイル構成

```
realtime-zunda/
├── main.py              # メインプログラム
├── requirements.txt     # Python依存関係
├── README.md           # このファイル
├── .gitignore          # Git除外ファイル
└── .env                # 環境変数（APIキー等）
```

## 必要な環境

### ソフトウェア要件

- Python 3.7以上
- VOICEVOX（音声合成エンジン）

### APIキー

- Google AI Studio APIキー（Gemini利用のため）

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-username/realtime-zunda.git
cd realtime-zunda
```

### 2. APIキーの設定

1. [Google AI Studio](https://aistudio.google.com/)でAPIキーを取得
2. プロジェクトルートに`.env`ファイルを作成
3. `.env`ファイルに以下の内容を追加：

```env
GOOGLE_API_KEY=your_actual_api_key_here
```

**注意**: `.env`ファイルには実際のAPIキーを設定し、GitHubにはコミットしないでください。

### 3. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 4. VOICEVOXのセットアップ

1. [VOICEVOX公式サイト](https://voicevox.hiroshiba.jp/)からVOICEVOXをダウンロード・インストール
2. VOICEVOXを起動する


## 使用方法

### 基本的な使い方

1. VOICEVOXを起動
   
    VOICEVOXを起動していないと応答が帰ってきません。

2. プログラムを実行

```bash
python main.py
```

3. 「どうぞ、話しかけてくださいのだ。」というメッセージが表示されたら、マイクに向かって話しかける
4. ずんだもんが音声で応答
5. 「さようなら」または「バイバイ」と言うと終了

### 設定のカスタマイズ

[`main.py`](main.py)で以下の設定を変更できます：

- `SPEAKER_ID`: VOICEVOXのキャラクターID（デフォルト: 3 = ずんだもん）
- `ZUNDAMON_PROMPT`: ずんだもんのキャラクター設定

## トラブルシューティング

### よくある問題

**音声認識ができない**
- マイクが正しく接続されているか確認
- マイクの音量設定を確認

**VOICEVOXに接続できない**
- VOICEVOXが起動しているか確認

**Gemini APIエラー**
- APIキーが正しく設定されているか確認
- Google AI StudioでAPIキーが有効か確認

## 依存関係

- `google-generativeai`: Google Gemini API
- `speechrecognition`: 音声認識
- `pyaudio`: 音声入出力
- `requests`: HTTP通信
- `pydub`: 音声データ処理
- `python-dotenv`: 環境変数の読み込み

## 注意事項

- VOICEVOXの利用規約に従ってご利用ください
- Google AI StudioのAPI利用制限にご注意ください
- マイクへのアクセス許可が必要です
