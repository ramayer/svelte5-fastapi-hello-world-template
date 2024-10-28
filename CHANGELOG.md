# Changelog


## 2024-10-27

* Install a [recent version of nodejs](https://nodejs.org/en/download/package-manager)
  * `nvm install 20`

* Create a sveltekit template
  * `npx sv create`

  * At this point a front-end app should work using 
    * `(cd frontend; npm run dev)`
  * It should be testable using
    * `(cd frontend; npm test)`
    * If the test fails you may need to manually run `npx playwright install`.   Tests will probably succeed.

* Create a hatch template
  * `hatch new backend`
  * At this point the backend should be testable using
    * `(cd backend; hatch test)`

* Add a fastapi app
  * Should be runnable using either of: 
    * `hatch run uvicorn backend.app.main:app --reload`
    * `hatch run backend`


