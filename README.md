# SRE-test

## Kubernetes Secret 변경
```shell
kubectl patch secret aws \
  -p "{\"data\":{
    \"AWS_ACCESS_KEY_ID\":\"$(echo -n '키 값' | base64)\",
    \"AWS_SECRET_ACCESS_KEY\":\"$(echo -n '시크릿 값' | base64)\"
  }}"
kubectl delete po sre-test-...

or
  
cd /kubernetes
deployment.yaml의 secret 값 수정
```

## API call
- /old-keys의 쿼리스트링으로 `N일`변수 처리 
```shell
curl 'Node IP':'Node Port'/old-keys\?days\='N일'
ex) curl 192.168.1.1:30000/old-keys\?days\=1000
  
or

http://192.168.1.1:30000/old-keys?days=1000 접속
```