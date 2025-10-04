from flask import Flask, request, jsonify

app = Flask(__name__)

# 假设的AI交互函数（根据您的描述无需实现）
def sendtoai(text):
    """
    将文本发送给AI Agent
    实际实现中这里会有AI API的调用逻辑
    """
    # 这里应该是将文本发送给AI的实际代码
    pass

def getfromai():
    """
    从AI获取回复
    实际实现中这里会获取AI的响应
    """
    # 这里应该是从AI获取响应的实际代码
    # 返回示例文本
    return "这是AI的回复"

@app.route('/ai', methods=['POST'])
def handle_ai_request():
    """
    处理AI请求的端点
    只接受POST请求，包含一段文字
    """
    try:
        # 检查请求内容类型
        if not request.is_json:
            return jsonify({"error": "请求必须是JSON格式"}), 400
        
        # 获取JSON数据
        data = request.get_json()
        
        # 检查是否包含文本
        if 'text' not in data:
            return jsonify({"error": "请求中必须包含'text'字段"}), 400
        
        text = data['text']
        
        # 验证文本是否为字符串且不为空
        if not isinstance(text, str) or not text.strip():
            return jsonify({"error": "文本内容不能为空"}), 400
        
        # 发送文本给AI
        sendtoai(text)
        
        # 获取AI回复
        ai_response = getfromai()
        
        # 返回AI回复
        return jsonify({
            "status": "success",
            "ai_response": ai_response
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"处理请求时发生错误: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
