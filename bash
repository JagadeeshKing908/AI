export OPENAI_API_KEY=your_api_key
docker build -t ai-agent .
docker run -d -p 8000:8000 ai-agent


Test:

curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{"prompt": "Hello AI"}'
