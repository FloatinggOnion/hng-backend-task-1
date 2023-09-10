from fastapi import FastAPI, Query
import uvicorn
from datetime import datetime, timedelta
import os


app = FastAPI()


@app.get('/api')
async def get_info(slack_name: str = Query(...), track: str = Query(...)):
    # Current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Current time with +/-2 validation
    utc_time = datetime.utcnow() + timedelta(hours=2)

    github_file_url = f'https://github.com/FloatinggOnion/hng-backend-task-1/{os.path.basename(__file__)}'
    github_repo_url = 'https://github.com/FloatinggOnion/hng-backend-task-1'

    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time.strftime("%Y-%m-%d %H:%M:%S"),
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return response


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)