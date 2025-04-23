from flask import Flask, request, Response
import json
from get_iam_info import check_old_access_keys

app = Flask(__name__)


@app.route('/old-keys', methods=['GET'])
def get_old_keys():
    # 쿼리스트링에서 hours 값을 받아오고, 없으면 기본값 24 사용
    old_access_keys = check_old_access_keys(request.args.get('hours', '24'))

    return Response(
        json.dumps(old_access_keys,ensure_ascii=False, indent=4, default=str),
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)