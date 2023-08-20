
import os
import re
import argparse
from autobook import Autobook


# 用于判断是否为连续的字符，且连续的字符数量等于传入的count
def contains_only_consecutive_chars(s, char, count):
    if re.search(rf"{char}{{{count + 1},}}", s):
        return False
    return bool(re.search(rf"{char}{{{count}}}", s))

def main():
    parser = argparse.ArgumentParser(description="Generate book outline or content.")
    parser.add_argument("book_name", type=str, help="Name of the book.")
    parser.add_argument("--generate", choices=["outline", "content"], required=True, help="Choose whether to generate outline or content.")
    parser.add_argument("--start_chapter", type=int, default=1, help="Chapter number to start content generation from (inclusive).")
    parser.add_argument("--end_chapter", type=int, default=1, help="Chapter number to end content generation at (inclusive).")

    args = parser.parse_args()

    model = Autobook()

    book_dir = f"./doc/{args.book_name}"
    if not os.path.exists(book_dir):
        os.makedirs(book_dir)

    if args.generate == "outline":
        print("开始生成大纲")
        outline = model.generate_outline(args.book_name)
        with open(f"{book_dir}/book_outline.md", "w", encoding='utf-8') as file:
            file.write(outline)
        print("大纲生成完毕")

    elif args.generate == "content":
        with open(f"{book_dir}/book_outline.md", "r", encoding='utf-8') as file:
            outline = file.readlines()

        chapter_index = 0

        for index, line in enumerate(outline):
            if contains_only_consecutive_chars(line, '#', 2):  # 假设使用"#"表示章节
                chapter_index += 1
                chapter_name = line.strip().split("##")[1].strip()

            if args.start_chapter <= chapter_index <= args.end_chapter and contains_only_consecutive_chars(line, '#', 3):  # 假设使用"##"表示小节
                section_title = line.strip().split("###")[1].strip()
                content = model.generate_section_content(args.book_name, chapter_name, section_title)

                with open(f"{book_dir}/{section_title}.md", "w", encoding='utf-8') as section_file:
                    section_file.write(content)
                print(f"第{chapter_index}章{section_title}节生成完毕")

if __name__ == "__main__":
    main()
