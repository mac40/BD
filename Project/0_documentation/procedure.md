# Procedure

## First Phase

1. similar sequences with blast
    * uniref90 preferably
    * ids result with cleaning and urllib.request uniprotkb for full fasta sequences
2. align with clustal-w
    1. take only a part of the sequences resulting from blast (find a suitable threshold (how???))
    2. clean the alignment by removing columns with less than 80% identity
3. use HMMER -> model classifing your group
    * analyze the result against the kinase_dataset to find a suitable lower score
    * use the score to choose the sequences with higher score on the result of the hmm against the human dataset
4. build an hmm for each of said sequences
    * evaluate them (how???)

---

## Second Phase (not really)

1. CD-HIT for clustering families (not mandatory...)