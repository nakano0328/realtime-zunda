import google.generativeai as genai

# --- ★★★ あなたのGoogle AI StudioのAPIキーをここに貼り付けてください ★★★
API_KEY = "your_api_key_here"

try:
    print(">> Gemini APIに接続を開始します...")
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    print(">> AIに「こんにちは」と送信します...")
    response = model.generate_content("こんにちは")
    
    print("\n--- AIからの返信 ---")
    print(response.text)
    print("--------------------")
    print("\n🎉 テスト成功！ APIキーとネットワーク接続は正常です。")

except Exception as e:
    print(f"\n❌ テスト失敗: エラーが発生しました。")
    print(f"エラー内容: {e}")
    print("\n【確認してください】")
    print("1. APIキーは正しいですか？ コピー＆ペーストの際に、前後に余分なスペースが入っていませんか？")
    print("2. Google AI Studioで、一度新しいAPIキーを発行して試してみてください。")
    print("3. 会社のネットワークなど、セキュリティが厳しい環境ではありませんか？")