# Frontend

## Technologies

The main technologies used for the frontend are:

1. **NGINX:** is open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more. 
1. **React:** is a free and open-source front-end JavaScript library for building user interfaces based on UI components. It is maintained by Meta (formerly Facebook) and a community of individual developers and companies. React can be used as a base in the development of single-page, mobile, or server-rendered applications with frameworks like Next.js. However, React is only concerned with state management and rendering that state to the DOM, so creating React applications usually requires the use of additional libraries for routing, as well as certain client-side functionality.
1. **MUI:** is a massive library of UI components designers and developers can use to build React applications. The open-source project follows Google's guidelines for creating components, giving you a customizable library of foundational and advanced UI elements. 

### React components

Class based components are not recommended since React 16. The following are different ways to create function based components:

```javascript
function ReactExampleComponent({ text }) {
  return (
    <div>
        <p>
            {text}
        </p>
    </div>
  );
}
```

```javascript
const ReactExampleComponent = ({ text }) => {
    // if you want to put logic here
  return (
    <div>
        <p>
            {text}
        </p>
    </div>
  );
}
```

```javascript
const ReactExampleComponent = ({ text }) => <div>
        <p>
            {text}
        </p>
    </div>
```


### How to add a new element

Given the previous component, we could add a MUI button adding:

```javascript
import { Button } from '@material-ui/core';

const ReactExampleComponent = ({ text }) => {
  const handleClick = () => {
    // do something
  }

  return <div>
        <p>
          <Button
            size='small'
            onClick={handleClick}
          >
            Text inside the button
          </Button>
        </p>
    </div>
}
```

Checkout the MUI components: 
https://mui.com/material-ui/

### How to add a new route

React Router DOM is an npm package that enables you to implement dynamic routing in a web app. It allows you to display pages and allow users to navigate them. It is a fully-featured client and server-side routing library for React.

Routes are stored in https://github.com/interlink-project/frontend/tree/master/react/src/routes

To add the route coproductionprocesses/:processId/mynewsection would be something like:

```javascript
...
const ReactExampleComponent = Loadable(lazy(() => import('../components/ReactExampleComponent')));
...

export const routes = [
  {
    path: 'dashboard',
    element: (
      <DashboardLayout />
    ),
    children: [
      {
        path: 'coproductionprocesses/:processId',
        children: [
          {
            path: '',
            element: <AuthGuard><CoproductionProcessProfile /></AuthGuard>
          },
          {
            path: 'mynewsection',
            element: <ReactExampleComponent>
          },
          ...
        ]
      },
      ...
    ],
  },
];
```
### How to add a new element in the sidebar

At the end of the day, the sidebar is a react component. At the time of writing, the sidebar code is at https://github.com/interlink-project/frontend/blob/master/react/src/components/navsidebars/ProcessSidebar.js.

The only thing you have to do is to add a new element in the *sections* variable:

```javascript
const sections = [

    {
      title: '',
      items: [
        {
          title: t('Overview'),
          path: `/dashboard/coproductionprocesses/${processId}/overview`,
          icon: <Dashboard />,
          disabled: false
        },
        ...
        {
          title: t('My new section'),
          path: `/dashboard/coproductionprocesses/${processId}/mynewsection`,
          icon: <Dashboard />,
          disabled: false
        },
      ]
    },
  ];
```

### File structure

```
.
├── Dockerfile                # file for generating the docker image based on the nginx official image
├── entrypoint.sh             # shell script to execute on container start
├── i18next-parser.config.js  # configuration of the translation files parser
├── jsconfig.json
├── nginx.conf                # configuration of nginx
├── node_modules              # javascript dependencies for the app
├── package-lock.json       
├── package.json              # dependencies and metadata of the application
├── public                    # public static files (not dynamic: css, images, favicon, main index.html used where react is imported...)
│   ├── _redirects
│   ├── index.html
│   └── static
└── src                       # files of the react app
    ├── App.js                # has the root component of the react app because every view and component are handled with hierarchy in React, where <App /> is the top most component in the hierarchy. This gives you the feel that you maintain hierarchy in your code starting from App.js.Other than that, you can have the App logic in the index.js file itself. But it's something related to conventions followed by the community using the library or framework. It always feels good to go along the community.
    ├── __api__               # calls to the API (coproduction / catalogue services)
    ├── axiosInstance.js      # axios (http library) customized object
    ├── components            # components of the application
    ├── configuration.js      # some environment variables
    ├── constants.js          # some constants
    ├── contexts
    ├── hooks
    ├── icons                 # some svg icons
    ├── index.js              # is the traditional and actual entry point for all node apps. Here in React it just has code of what to render and where to render.
    ├── pages                 # at the end of the day, they are components, but those ones used by the routes
    ├── routes                # specification of the routes of the application
    ├── slices
    ├── store
    ├── theme                 # variables of the theme of the app
    ├── translations          # translation files and i18n object
    └── utils                 # some generic utils
```

### Translations

### API calls

### State management