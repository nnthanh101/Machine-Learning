import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'OceanSoft',
  tagline: 'Digital & AI Transformation',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://oceansoft.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'nnthanh101',  // Usually your GitHub org/user name.
  projectName: 'machine-learning', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/nnthanh101/Machine-Learning/tree/main/docs/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/nnthanh101/Machine-Learning/tree/main/docs/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'OceanSoft',
      logo: {
        alt: 'Digital and AI Transformation',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'dataScienceSidebar',
          position: 'left',
          label: 'Data Science',
        },
        {
          type: 'docSidebar',
          sidebarId: 'machineLearningSidebar',
          position: 'left',
          label: 'Machine Learning',
        },
        {
          type: 'docSidebar',
          sidebarId: 'artificialIntelligenceSidebar',
          position: 'left',
          label: 'Artificial Intelligence',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/nnthanh101/Machine-Learning/tree/main/docs',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Data Science',
              to: '/docs/data-science',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/nnthanh101',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/facebook/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © 2003-${new Date().getFullYear()} <a href="https://www.linkedin.com/in/nnthanh" target="_blank" rel="noopener noreferrer">OceanSoft.io</a>`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
