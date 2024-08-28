# Vokalräkning

vokaler = "aeiouyåäöAEIOUYÅÄÖ"
mening = input()
räknare = 0

for vokal in mening:
    if vokal in vokaler:
        räknare += 1
print(räknare)