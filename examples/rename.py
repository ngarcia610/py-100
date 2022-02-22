# Renames files in a directory
# Author: Nathan Garcia

import os

os.chdir('S:/Videos/Home Movies/2009')
count = 1

# Split the filename into 2 parts: filename and extension
# Rename the file
# Combine and write out the change
for f in os.listdir():
  file_name, file_ext = os.path.splitext(f)
  file_name = '2009_' + str(count) + file_ext
  count += 1
  print(file_name)
  os.rename(f, file_name)
