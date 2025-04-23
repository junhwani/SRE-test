# SRE-test

## Kubernetes Secret 변경
```shell
kubectl patch secret aws \
  -p "{\"data\":{
    \"AWS_ACCESS_KEY_ID\":\"$(echo -n '키 값' | base64)\",
    \"AWS_SECRET_ACCESS_KEY\":\"$(echo -n '시크릿 값' | base64)\"
  }}"
```