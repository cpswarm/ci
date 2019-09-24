# Frevo CI

## Test
```bash
git clone https://github.com/cpswarm/ci.git
cd ci/frevo
git clone https://git.repository-pert.ismb.it/mrappaport/cpswarm.git repo
docker build -t frevo-test .
docker run -v $(pwd)/hashes:/home/frevo/testsuite/hashes --rm frevo-test -renew
docker run -v $(pwd)/hashes:/home/frevo/testsuite/hashes --rm frevo-test
```