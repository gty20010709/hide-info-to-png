from stegano import lsb


def hide_info(image_path: str, message: str, output_path: str):
    # 将Base64字符串隐藏在图片中
    secret = lsb.hide(image_path, message=message)
    secret.save(output_path)

def extract_info(image_path: str) -> str:
    # 从图片中提取Base64字符串
    return lsb.reveal(image_path)