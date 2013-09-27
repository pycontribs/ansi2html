Changelog
=========

0.10.0
------

- Add trove for py3.3. `683f672fa <https://github.com/ralphbean/ansi2html/commit/683f672fa6071cc7390b6c64858127fe0b1e2e77>`_
- Stop adding unwanted spaces (issue 26) `b5163a80f <https://github.com/ralphbean/ansi2html/commit/b5163a80feea7f6ba8879357524ccbe143e68281>`_
- Add test for issue 25 `6df79eb8b <https://github.com/ralphbean/ansi2html/commit/6df79eb8b95b2c36e7395bedcd13e0facb323434>`_
- Fix destructive reset marker handling (issue 25) `4db97b126 <https://github.com/ralphbean/ansi2html/commit/4db97b126c600d30a922ab5899faa8879f699739>`_
- Fix ANSI code decoding (issue 25) `f277f8f3c <https://github.com/ralphbean/ansi2html/commit/f277f8f3c4eaa1256c5df66238583b5a69882456>`_
- Fix writing to sys.stdout.buffer `7a3267d53 <https://github.com/ralphbean/ansi2html/commit/7a3267d53a2ea61a0af6021faedf154ba89b2f87>`_
- Add convenience Makefile `8d3f3e055 <https://github.com/ralphbean/ansi2html/commit/8d3f3e055e679bf723d6a846fbff2c95a7224b9a>`_
- Merge pull request #30 from hartwork/makefile `156bc89da <https://github.com/ralphbean/ansi2html/commit/156bc89da97c7de19b2beb8e2de7bde2f2535a20>`_
- Merge pull request #29 from hartwork/issue_29 `8495723ae <https://github.com/ralphbean/ansi2html/commit/8495723ae8e057248537a53f9e7e800547d6640e>`_
- Merge pull request #27 from hartwork/issue_26 `74d237c18 <https://github.com/ralphbean/ansi2html/commit/74d237c18165625bedde85e25f1eb988f0da8ca1>`_
- Merge pull request #28 from hartwork/issue_25 `8c77f6d93 <https://github.com/ralphbean/ansi2html/commit/8c77f6d93754c03fc256754de73b8b2bf1d6c08c>`_
- Fix italic to be font-style (rather than font-weight) `47b533b6d <https://github.com/ralphbean/ansi2html/commit/47b533b6de62ebe97d32322eaa3a5dcec735a077>`_
- Add inv* CSS classes `408808197 <https://github.com/ralphbean/ansi2html/commit/408808197e9b33aa55210b5f03940267b3e01c83>`_
- Handle state in code, not in HTML; support more ANSI codes `fce66a6a9 <https://github.com/ralphbean/ansi2html/commit/fce66a6a905fb6aa006cfa1f6ad4716ebb46e63b>`_
- Adapt tests to new approach to state `49046c620 <https://github.com/ralphbean/ansi2html/commit/49046c620079d3a325753081ba99b1deb0c8287a>`_
- Add CSS classes for lighter font style (2), blinking (5/6), hidden text (8) `e488daca3 <https://github.com/ralphbean/ansi2html/commit/e488daca38176c9cdba7318a958fc79bfb16f9cb>`_
- Save producing no-op span tags `340620f88 <https://github.com/ralphbean/ansi2html/commit/340620f88b66a686c16f155465f172321fe39cff>`_
- Test ANSI codes that just turned supported `f4774bcf0 <https://github.com/ralphbean/ansi2html/commit/f4774bcf0005175bc00f282f73365fa59b6f47fb>`_
- Make code testing pairs of files re-usable `f95ca305d <https://github.com/ralphbean/ansi2html/commit/f95ca305dba5951c25178fc12fb0e206120aa1b4>`_
- Add testcase for output from "eix -I svn -F" `e3f593671 <https://github.com/ralphbean/ansi2html/commit/e3f59367174fb9ed4df2d19ed012bae45f0ce2ce>`_
- Merge pull request #31 from hartwork/font-style-italic `a25950fe6 <https://github.com/ralphbean/ansi2html/commit/a25950fe6f0bdd12c92cbbd2109655bfd1cc5a36>`_
- Tweak for py3 support. `9766508e1 <https://github.com/ralphbean/ansi2html/commit/9766508e16007fdcd764ba52c79af798d8d816fd>`_
- Add py3.3 to travis config. `ceef1eb8e <https://github.com/ralphbean/ansi2html/commit/ceef1eb8e83a58fe895f67185f4242b8e49f7b7c>`_
- Merge branch 'stateful' into develop `29868b6ec <https://github.com/ralphbean/ansi2html/commit/29868b6ec1e742a23e3b60db17f187ce75bb3d57>`_

0.9.4
-----

- Fix encoding issue. `64881f549 <https://github.com/ralphbean/ansi2html/commit/64881f549126f5c576df7b75e70e49633fe59337>`_
- Silence silly py2.7 test errors. `b5db644ff <https://github.com/ralphbean/ansi2html/commit/b5db644ffa29497bd16dc0f0adae7f0847603f2c>`_
