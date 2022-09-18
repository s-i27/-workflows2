# -workflows2
## [ADR](https://github.com/npryce/adr-tools)
### ref https://qiita.com/fuubit/items/dbb22435202acbe48849
決定事項の経緯や背景を第三者が閲覧可能
軽量なドキュメンテーション
第三者が簡単にコメント

### NEW ADR

```
adr new ADR導入の検討
```

### Replacement  ADR

```
adr new -s 1 ADRやめた
```

良いADRの特徴：
ポイントインタイム(Point in Time)
決定が作成された時を特定できる。

合理性(Rationality)
その決定が作成された理由を説明する。

イミュータブルレコード(Immutable record)
以前に公表されたADRでなされた決定は変更されるべきではない。

特異性(Specificity)
各ADRは単一の決定についてであるべき。




https://zenn.dev/dzeyelid/articles/77541fe1336951
python
https://zenn.dev/sotahi/articles/438a5b733e7331
