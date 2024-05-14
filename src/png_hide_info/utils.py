import base64
import os
import subprocess


def chmod_and_run(file_path):
    """为文件设置可执行权限并执行它"""
    try:
        # 设置文件的可执行权限
        os.chmod(file_path, os.stat(file_path).st_mode | 0o111)

        # 执行文件
        result = subprocess.run(file_path, capture_output=True, text=True)

        # 返回执行结果
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }
    except Exception as e:
        return str(e)


def bin_to_base64(bin_file_path):
    """读取二进制文件并转换为 Base64 编码的字符串"""
    try:
        with open(bin_file_path, "rb") as file:
            binary_data = file.read()
        base64_encoded_data = base64.b64encode(binary_data)
        return base64_encoded_data.decode("utf-8")
    except Exception as e:
        return str(e)


def bin_from_base64(base64_string, output_file_path):
    """将 Base64 编码的字符串解码并保存为二进制文件"""
    try:
        base64_decoded_data = base64.b64decode(base64_string)
        with open(output_file_path, "wb") as file:
            file.write(base64_decoded_data)
        return "文件保存成功"
    except Exception as e:
        return str(e)


def str_to_base64(message: str) -> str:
    # 将中文信息编码为Base64
    message_bytes = message.encode("utf-8")
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode("utf-8")


def str_from_base64(base64_message: str) -> str:
    # 将Base64字符串解码回原始中文信息
    base64_bytes = base64_message.encode("utf-8")
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode("utf-8")
