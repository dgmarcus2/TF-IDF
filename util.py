def read_data(filename):
  with open(filename,'r') as fd:
    return fd.read()

def split_chapters(data):
  import re
  pattern = r'^CHAPTER\s[A-Z\s]+\.?$'
  #pattern = r'CHAPTER\s[A-Z\s]+'
  regex = re.compile(pattern, re.M)
  return regex.split(data)

def tokenize_prep(data):
  import re
  # how to treat: you-did—I-didn't
  pattern = r"[A-Za-z0-9']+-?[A-Za-z0-9']+"
  #pattern = r"[A-Za-z0-9']+"
  regex = re.compile(pattern)
  tokens = regex.findall(data)
  t = [t.strip("'") for t in tokens] # just leading and trailing
  return " ".join(t)

def clean_chapter(chapter):
  c = chapter.replace("\n", " ")
  return c.strip()

def clean_chapters(chapters):
  out = []
  for i, c in enumerate(chapters):
    c = clean_chapter(c)
    if len(c) > 0:
      out.append(tokenize_prep(c))
  return out

def split_into_tokens(data, normalize=True):
  tokens = data.split()
  if normalize:
    tokens = [t.lower() for t in tokens if len(t) > 2]
  return tokens
