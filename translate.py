from googletrans import Translator
import time
import os

translator = Translator()

input_file = "English_Sub.srt" # file to translate
output_file = "Chinese_Sub.srt" # output translated text folder

DELAY = 0.5

def is_subtitle_text(line):
    """check if line is actual subtitle text (not numbering or timing)."""
    return line.strip() and not line.strip().isdigit() and "-->" not in line

with open(input_file, "r", encoding="utf-8") as f_in, \
     open(output_file, "a", encoding="utf-8") as f_out:

    for idx, line in enumerate(f_in, start=1):
        if is_subtitle_text(line):
            try:
                translated = translator.translate(line.strip(), src="en", dest="zh-cn").text #zh-cn can be changed to other languages
                f_out.write(translated + "\n")
                print(f"[OK] {line.strip()}  ➜  {translated}")
            except Exception as e:
                f_out.write(line)
                print(f"[ERROR] {e} — kept original: {line.strip()}")
            time.sleep(DELAY)
        else:
            f_out.write(line)

        f_out.flush()
        os.fsync(f_out.fileno())

print("✅ Translation complete! Output saved to", os.path.abspath(output_file))
