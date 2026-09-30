# Readability check for an RSQKit task page (body text only).
# Usage: python3 readability.py page.md   (needs: pip install textstat)
import re, sys, textstat
text = open(sys.argv[1], encoding="utf-8").read()
text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)          # front matter
text = text.split('\n## Further Reading')[0]                        # body only
text = re.sub(r'```.*?```', '', text, flags=re.S)                   # code blocks
text = re.sub(r'^#+ .*$', '', text, flags=re.M)                     # headings
text = re.sub(r'\{% tool "([^"]+)" %\}', r'\1', text)               # tool tags
text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)                # inline links
text = re.sub(r'\[([^\]]+)\]\[[^\]]*\]', r'\1', text)               # reference links
text = re.sub(r'^\s*[-*] ', '', text, flags=re.M)                   # list markers
words = textstat.lexicon_count(text)
sentences = textstat.sentence_count(text)
print(f"Words: {words}")
print(f"Average sentence length: {words / max(sentences, 1):.1f}")
print(f"Gunning Fog: {textstat.gunning_fog(text):.1f}")
print(f"Flesch Reading Ease: {textstat.flesch_reading_ease(text):.1f}")
