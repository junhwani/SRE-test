import boto3
from datetime import datetime, timezone

def check_old_access_keys(hours):
    iam = boto3.client('iam')

    # 현재 날짜
    current_date = datetime.now(timezone.utc)

    # 저장할 결과값
    old_keys = []

    # 모든 사용자 조회
    users = iam.list_users()

    for user in users['Users']:
        username = user['UserName']

        # 사용자의 액세스 키 조회
        keys = iam.list_access_keys(UserName=username)

        for key in keys['AccessKeyMetadata']:
            key_id = key['AccessKeyId']
            status = key['Status']
            create_date = key['CreateDate']

            # 생성일부터 현재까지의 일수 계산
            key_age_hours = (current_date - create_date).total_seconds() / 3600

            # 지정된 일수를 초과한 키 확인 후 저장
            if key_age_hours > float(hours):
                old_keys.append({
                    'UserName': username,
                    'AccessKeyId': key_id
                })

    return old_keys