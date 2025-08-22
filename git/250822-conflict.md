# Conflict

## Situation 1. merge

```shell
git merge main
vi {filename}
git add {filename}
git commit
```

## Situation 2. rebase

```shell
git branch rb-test
git switch rb-test
git rebase main
git add {filename}
git rebase --continue
```
