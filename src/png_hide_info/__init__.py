from png_hide_info.core import hide_info, extract_info
from png_hide_info.utils import str_to_base64, str_from_base64, bin_to_base64, bin_from_base64, chmod_and_run



def hide_and_extract_str_demo() -> None:
    original_message = "你好世界 来自中文字符串"
    image_path = "res/hello.png"
    output_path = "res/hello_hide.png"
    hide_info(image_path, str_to_base64(original_message), output_path)
    extracted_message = str_from_base64(extract_info(output_path))
    print(extracted_message)


def hide_and_extract_bin_demo() -> None:
    original_hello_bin = "res/hello"
    output_hello_bin = "res/hello_out"
    image_path = "res/hello.png"
    output_path = "res/hello_hide.png"
    hide_info(image_path, bin_to_base64(original_hello_bin), output_path)
    extract_result = bin_from_base64(extract_info(output_path), output_hello_bin)
    print(extract_result)
    run_result = chmod_and_run(output_hello_bin)
    print(run_result)




def main() -> int:
    hide_and_extract_str_demo()
    hide_and_extract_bin_demo()
    return 0
