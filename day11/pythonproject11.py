import os
import threading


# 1
# def rename_files(old_dir, new_dir, filename):
#     old_path = os.path.join(old_dir, filename)
#     new_path = os.path.join(new_dir, filename)

#     try:
#         os.rename(old_path, new_path)
#         print(f"重命名文件：{old_path} -> {new_path}")
#     except Exception as e:
#         print(f"无法重命名文件 {old_path}: {e}")

# old_directory = '/path/to/old_directory'
# new_directory = '/path/to/new_directory'


# file_list = os.listdir(old_directory)   #仅示例，实际输入路径，new_dictory同理
# # 创建线程
# threads = []
# for filename in file_list:
#     thread = threading.Thread(target=rename_files, args=(old_directory, new_directory, filename))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# print("------")


# 2
import threading
from googletrans import Translator
from http.server import BaseHTTPRequestHandler, HTTPServer

class TranslateServer(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        query = self.path.split('?')[1]
        text = query.split('=')[1]
        translated_text = translator.translate(text, src='en', dest='fr').text
        self.wfile.write(translated_text.encode())

def run(server_class=HTTPServer, handler_class=TranslateServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting translation server on port {port}")
    httpd.serve_forever()

translator = Translator()

# 创建多线程翻译服务器
if __name__ == '__main__':
    server_thread = threading.Thread(target=run)
    server_thread.start()



# ChatGPT：在上述示例中，我们使用googletrans库进行文本翻译。我们创建一个基本的HTTP服务器，
# 它监听指定的端口（8080），接受GET请求，从查询参数中提取文本，
# 然后将其翻译为指定语言（在此示例中是从英语到法语）并将翻译后的文本返回给客户端。
# 你可以在不同的线程中运行多个翻译请求，这样服务器就可以同时处理多个翻译请求。请确保你已经替换成适用于你的API密钥和翻译源语言、目标语言。
# 这个示例是一个基本的起点，你可以根据需求对其进行扩展和改进。