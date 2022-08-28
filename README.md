# -workflows2
バックエンド刷新チームでは以下のことに着目してADRの考え方をドキュメンテーションに取り入れました。

決定事項の経緯や背景を第三者が閲覧可能
軽量なドキュメンテーション
第三者が簡単にコメント、編集可能
aaaaaa

# GitHub Actions Workflow Best Practices
https://zenn.dev/tmknom/books/github-organization-security/viewer/github-actions

https://developers.cyberagent.co.jp/blog/archives/36423/#github-actions-workflow-best-practices

timeout-minutes で最大実行可能時間を指定

## セキュリティリスク
permissions で GITHUB_TOKEN の権限を管理
Commit hash 指定
OIDC により管理する認証情報を減らす
利用する Action の継続的アップデート(Dependabot)
