import pytube

from pytube import YouTube

def banner():
	print("""\033[32m
██╗   ██╗████████╗   ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗
╚██╗ ██╔╝╚══██╔══╝   ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝    ██║█████╗███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
  ╚██╔╝     ██║╚════╝╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
   ██║      ██║      ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
   ╚═╝      ╚═╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝\033[0m
\033[30;42mScrape YouTube Videos using Python\033[0m\n""")
banner()

link = input("\033[1;32mEnter the video link :\033[0m ")
j = YouTube(link)

print("\033[1;33m+---------------------+")
print("| \033[1;32m--- INFORMATION ---\033[1;33m |")
print("+---------------------+\033[0m")
print("\033[1;32mJudul :\033[0m",j.title)
print("\033[1;32mDeskripsi :\033[0m",j.description)
print("\033[1;32mPenayangan :\033[0m",j.views)
print("\033[1;32mUsia Dibatasi :\033[0m",j.age_restricted)
print("\033[1;32mPanjang Video :\033[0m",j.length)
print("\033[1;32mTanggal Publikasi :\033[0m",j.publish_date)
print("\033[1;32mRating :\033[0m",j.rating)
print("\033[1;32mTag :\033[0m",j.keywords)
print("\033[1;32mURL Thumbnail :\033[0m",j.thumbnail_url)
print("\033[1;32mURL Channel :\033[0m",j.channel_url)
print("\033[1;32mChannel :\033[0m",j.author)
print("\033[1;32mID Channel :\033[0m",j.channel_id)
