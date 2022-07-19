# https://stackoverflow.com/a/52269934/2839786

#git clone \
#  --depth 1  \
#  --filter=blob:none  \
#  --sparse \
#  https://github.com/cirosantilli/test-git-partial-clone \
#;
#cd test-git-partial-clone
#git sparse-checkout set d1
#
#cd ..

# clone "algorithms" code
git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/keon/algorithms \
;
cd algorithms
git sparse-checkout set algorithms

cd ..

# clone "keras" code
git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/keras-team/keras \
;
cd keras
git sparse-checkout set keras

cd ..

# clone "PyTorch Tutorial" code
git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/yunjey/pytorch-tutorial \
;
cd pytorch-tutorial
git sparse-checkout set tutorials

cd ..

# clone "Scikit-Learn" code
git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/scikit-learn/scikit-learn \
;
cd scikit-learn
git sparse-checkout set sklearn