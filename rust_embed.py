import embed_anything

from embed_anything import EmbedData
import time
start = time.time()
data = embed_anything.embed_file("test_paper.pdf")

print(data[0])

end = time.time()
print("time is: ", end - start)