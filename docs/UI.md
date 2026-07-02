# DOCUMENT 4 — UI/UX Brief
 
## 4.1 Design Philosophy
Dark, data-dense, cyberpunk-professional — financial-terminal feel with modern SaaS polish. Prioritize scannability: KPI cards and charts over walls of text.
 
## 4.2 Color Palette
- Background: `#0A0E14` (near-black)
- Surface: `#131A24`
- Primary accent: `#00E5FF` (cyan)
- Risk colors: Low `#22C55E`, Medium `#F59E0B`, High `#EF4444`
- Text: `#E6EDF3` primary, `#8B96A5` secondary
## 4.3 Typography
Headings: Space Grotesk / Sora (technical, modern). Body: Inter. Monospace for numbers/tickers: JetBrains Mono.
 
## 4.4 Design System
Card-based layout, 8px spacing grid, rounded-lg corners (8-12px), subtle glow on accent elements, consistent iconography (Lucide icons).
 
## 4.5 Dashboard Layout
Left sidebar (nav: Dashboard, Documents, Compare, Portfolio, Alerts, Admin) → top bar (company selector, search, profile) → main grid (KPI cards → charts → risk heatmap → recommendation panel).
 
## 4.6 States
- **Loading:** skeleton cards, animated processing pipeline indicator
- **Empty:** "Upload your first report" prompt with illustration
- **Error:** inline error card with retry action, never a blank screen
## 4.7 Accessibility
Sufficient contrast ratios despite dark theme, keyboard navigation, ARIA labels on charts, alt text on icons.
 
## 4.8 Wireframe Descriptions (key screens)
- **Login/Register:** centered card, minimal, dark background with subtle grid pattern
- **Dashboard:** 3-column KPI card row, 2-column chart row, full-width risk heatmap, sidebar chat toggle
- **Document Detail:** PDF preview pane (left) + extracted insights pane (right) with citation highlighting
- **Compare:** side-by-side split view, synced scroll
- **Admin:** table-heavy, dense data grid style
