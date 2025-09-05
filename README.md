# 🎬 Subtitle Translator

This project lets you **extract subtitles from an `.mkv` movie** and **translate them into another language** (e.g. English → Chinese).

---

## 📦 Requirements

- **Python 3.12+**
- [`googletrans`](https://pypi.org/project/googletrans/)  
  Install with:
  ```bash
  pip install googletrans==4.0.0-rc1
  ```
- [FFmpeg](https://ffmpeg.org/download.html) (must be available in your system PATH)

---

## 📖 Usage

### 1. Inspect subtitle tracks in your `.mkv`
Run:
```bash
ffmpeg -i <movie_name>.mkv
```

Look for subtitle streams in the output. Example:
```
Stream #0:3(eng): Subtitle: ass (ssa)
    Metadata: title : Signs & Songs
Stream #0:4(eng): Subtitle: ass (ssa)
    Metadata: title : English Sub
Stream #0:5(jpn): Subtitle: ass (ssa)
    Metadata: title : Japanese
```

Here, `#0:4` is the English subtitle we want.

---

### 2. Extract the subtitle you want
Use `-map` with the correct stream index:
```bash
ffmpeg -i <movie_name>.mkv -map 0:4 English_Sub.srt
```

Now you’ll have `English_Sub.srt`.

---

### 3. Translate subtitles
Edit `translate.py`:

- **Line 7 & 8** → set your input and output filenames (e.g. `"English_Sub.srt"` → `"Chinese_Sub.srt"`)
- **Line 22** → change the target language code (`"zh-cn"` for Simplified Chinese, `"zh-tw"` for Traditional Chinese, etc.)

Run:
```bash
python translate.py
```

The script will:
- Read each subtitle line.
- Translate it using Google Translate.
- Save the translated subtitles to your output file.

---

## 🌍 Supported Languages

The script uses [Google Translate language codes](https://cloud.google.com/translate/docs/languages).  
Examples:
- `zh-cn` → Simplified Chinese
- `zh-tw` → Traditional Chinese
- `ja` → Japanese
- `fr` → French
- `es` → Spanish

---

## ⚠️ Notes
- The translation uses the free `googletrans` library (unofficial). It may be **rate-limited** or unstable if you translate very large files.  
- If Google blocks requests, re-run the script — it will pick up where it left off if you use the resumable version.  
- For the best quality, consider a paid API like **DeepL** or **Google Cloud Translate**.

---

## ✅ Example

```bash
# Step 1: Inspect streams
ffmpeg -i "A Whisker Away.mkv"

# Step 2: Extract English subtitle
ffmpeg -i "A Whisker Away.mkv" -map 0:4 English_Sub.srt

# Step 3: Translate to Simplified Chinese
python translate.py
```

Result → `Chinese_Sub.srt`
