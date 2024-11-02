# intro2AI
This is practice

1. Create virtual environment (VE) in Codespaces: virtualenv myENV
2. Codespaces Terminal:
     1.  Activate VE: source myENV/bin/activate
     2.  Create Makefile: touch Makefile
     3.  Create requirements.txt: touch requirements.txt
     4.  Run install: make install
     5.  Run test: make test
     6.  Git Push: git add*, git commit -m "adding makefile", git push, git rebase (if there is repo contains different content from Codespaces)
3. 2 ways to share Colab notebook with public Github: 1. Select Save softcopy in Github from Colab/File, 2. Share Link from Google drive: Copy link from Google drive and paste in Readme as in: https://colab.research.google.com/drive/1ua-_242OoVj33vRGfZyMNrKGzWJ3dLzo?usp=sharing

4. Copy selected file from Github to Codespaces: git checkout main -- helloAI.ipynb\\
5. Added hello.py for Injest function, and test_hello.py to test the assertion on the return dataframe
