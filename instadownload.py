import instaloader

profile_name = input("Enter Insta Profil Name: ")

print("Downloading Media... ")

instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)

print("Download Completed!")