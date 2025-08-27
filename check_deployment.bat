@echo off
echo ============================================================
echo PSO+Zscore - Checking Railway Deployment
echo ============================================================
echo.

echo Your Railway URLs:
echo Dashboard: https://railway.app/project/cd882d82-3b5a-41ba-882f-37e8b961224e
echo Service: https://railway.app/project/cd882d82-3b5a-41ba-882f-37e8b961224e/service/9ef5f530-f52a-4f81-aaf4-5669174c3e59
echo.

echo App URL: https://3pso-zscore-production.up.railway.app/
echo.

echo Current Status: Application returning 404
echo.
echo Possible issues:
echo 1. Deployment might still be building
echo 2. Backend service might not be running
echo 3. Port configuration might be incorrect
echo.

echo To check deployment status:
echo 1. Open Railway dashboard (opening now)
echo 2. Check the "Deployments" tab for build status
echo 3. Check "Logs" tab for any errors
echo 4. Verify environment variables are set
echo.

start https://railway.app/project/cd882d82-3b5a-41ba-882f-37e8b961224e/service/9ef5f530-f52a-4f81-aaf4-5669174c3e59?environmentId=f17be55a-922a-4d0f-acc0-98aebc48d677

echo If deployment failed, you can:
echo 1. Click "Redeploy" in Railway dashboard
echo 2. Check logs for errors
echo 3. Verify Dockerfile is correct
echo 4. Ensure environment variables are set
echo.

pause