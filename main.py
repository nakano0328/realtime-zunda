import google.generativeai as genai
import speech_recognition as sr
import requests
import io
from pydub import AudioSegment
from pydub.playback import play

# --- 設定項目 ---
# Google AI Studioで取得したAPIキーを設定
GOOGLE_API_KEY = "your_api_key_here"  # ここにAPIキーを入力してください

# VOICEVOXのキャラクターID (ずんだもんのノーマルスタイルは3)
SPEAKER_ID = 3

# Geminiに与えるキャラクター設定
ZUNDAMON_PROMPT = """
あなたは「ずんだもん」というキャラクターです。
以下のルールに従って、ユーザーと会話してください。

# ルール
- 東北訛りの元気な女の子として振る舞ってください。
- 一人称は「ボク」です。
- 口癖は「〜のだ」「〜なのだ」です。
- ユーザーからの質問には、元気いっぱいに、少しお茶目に答えてください。
"""

# --- 初期設定 ---
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')
chat = model.start_chat(history=[
    {'role': 'user', 'parts': [ZUNDAMON_PROMPT]},
    {'role': 'model', 'parts': ["わかったのだ！ボクはずんだもんなのだ！"]}
])

def speak_zundamon(text):
    """VOICEVOX APIを使ってテキストを音声合成し再生する関数"""
    try:
        # 1. audio_query（音声合成用のクエリを作成）
        res_query = requests.post(
            f'http://127.0.0.1:50021/audio_query?speaker={SPEAKER_ID}&text={text}'
        )
        res_query.raise_for_status()
        query_data = res_query.json()

        # 2. synthesis（音声ファイルを生成）
        res_synth = requests.post(
            f'http://127.0.0.1:50021/synthesis?speaker={SPEAKER_ID}',
            json=query_data
        )
        res_synth.raise_for_status()

        # 3. 音声データを再生
        audio = AudioSegment.from_file(io.BytesIO(res_synth.content), format="wav")
        play(audio)

    except requests.exceptions.RequestException as e:
        print(f"VOICEVOX APIへの接続に失敗しました: {e}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def main():
    """メインの会話ループ"""
    r = sr.Recognizer()
    mic = sr.Microphone()

    print("どうぞ、話しかけてくださいのだ。")

    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source) # 周囲のノイズに適応
            audio = r.listen(source)

        try:
            # GoogleのWeb Speech APIで音声をテキストに変換
            user_text = r.recognize_google(audio, language='ja-JP')
            print(f"あなた: {user_text}")

            if "さようなら" in user_text or "バイバイ" in user_text:
                response_text = "また話そうなのだ！バイバイなのだ！"
                print(f"ずんだもん: {response_text}")
                speak_zundamon(response_text)
                break

            # Geminiに応答を生成させる
            print(">> Geminiに問い合わせ中...")
            response = chat.send_message(user_text, stream=True)
            
            response_text = ""
            try:
                for chunk in response:
                    response_text += chunk.text
                
                print(">> Geminiからの応答:", response_text) # ★AIの応答内容をコンソールに表示

                if not response_text:
                    print(">> エラー: Geminiから空の応答が返ってきました。")
                    continue # 問題があればループの先頭に戻る

            except Exception as e:
                print(f">> Geminiからの応答受信中にエラーが発生しました: {e}")
                continue # 問題があればループの先頭に戻る


            print(f"ずんだもん: {response_text}")

            # ずんだもんが話す
            print(">> VOICEVOXで音声合成を開始します...") # ★追加
            speak_zundamon(response_text)
            print(">> 音声の再生が完了しました。") # ★追加

        except sr.UnknownValueError:
            print("ごめんなさい、うまく聞き取れなかったのだ。もう一度言ってほしいのだ。")
        except sr.RequestError as e:
            print(f"音声認識サービスからの結果をリクエストできませんでした; {e}")

if __name__ == '__main__':
    main()