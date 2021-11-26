from github import Github

a=Github("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").get_repo("luoky76/GCat")
print(a.get_languages())