# -*- coding: utf-8 -*-
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'builders' else SCRIPT_DIR

manifest_path = os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')
if not os.path.exists(manifest_path):
    manifest_path = os.path.join(ROOT_DIR, 'scratch', 'logo_manifest.json')

with open(manifest_path, 'r', encoding='utf-8') as f:
    logo_manifest = json.load(f)

client_cards_list = []
for item in logo_manifest:
    brand = item['name'].replace('"', '&quot;')
    fn = item['filename']
    client_cards_list.append(f'''                <div class="client-brand-card" title="{brand}">
                  <img src="assets/client_logos/{fn}" alt="{brand}" loading="lazy" />
                </div>''')
client_cards_html = '\n'.join(client_cards_list)

slides_data = [
    {
        'num': 1,
        'tag': '01 // SOLUTIONS MATRIX',
        'title': 'AI Industry Solutions',
        'type': 'manifesto',
        'html': '''
          <div class="slide-manifesto-layout">
            <div class="manifesto-card-stage">
              <div class="manifesto-headline-box">
                <h1 class="manifesto-line-2 vision-title-text">INTELLIGENT INDUSTRY<br><span class="highlight-red-text">SOLUTIONS</span></h1>
                <div class="manifesto-accent-line"></div>
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 2,
        'tag': '02 // SMART PREMISES',
        'title': 'Smart Premises Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + 6 Topics -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Smart Premises <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A technology-driven system that integrates automation, sensors, and AI to manage and monitor buildings, enhancing security, energy efficiency, comfort, and operational control in residential, commercial, or industrial spaces through real-time data, remote access, and smart devices.
                </p>
              </div>

              <!-- All 6 Solution Topics (Titles Only, No Inner Content) -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: Audio & Video Solutions -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                      <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.08"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Audio & Video Solutions</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 2: GPS & Drone Solutions -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="3"></circle>
                      <path d="M12 2v3m0 14v3M2 12h3m14 0h3"></path>
                      <path d="m4.93 4.93 2.12 2.12m9.9 9.9 2.12 2.12M4.93 19.07l2.12-2.12m9.9-9.9 2.12-2.12"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">GPS & Drone Solutions</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 3: Customizable Software Solutions -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="16 18 22 12 16 6"></polyline>
                      <polyline points="8 6 2 12 8 18"></polyline>
                      <line x1="14" y1="4" x2="10" y2="20"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Customizable Software Solutions</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 4: Video Surveillance -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-red">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path>
                      <circle cx="12" cy="13" r="4"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Video Surveillance</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 5: Video Analytics -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M2 12h5l3 7 4-14 3 7h5"></path>
                      <circle cx="12" cy="12" r="1"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Video Analytics</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 6: Command and Control Centre -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-slate">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                      <line x1="8" y1="21" x2="16" y2="21"></line>
                      <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Command and Control Centre</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

              </div>
            </div>

            <!-- Right Column: Smart Premises & Drone Telemetry Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/smart_premises_visual.jpg" alt="Smart Premises AI Drone & Command Center" class="analytics-matrix-img" onerror="this.src='assets/cover_ai_neural_brain.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 3,
        'tag': '03 // AI CAPABILITIES',
        'title': 'AI Used Cases',
        'type': 'content',
        'html': '''
          <div class="slide-usecases-split-layout">
            <!-- Left Column: Exact PPT 12 Checkmark Items -->
            <div class="usecases-left-column">
              <div class="usecases-header-block">
                <h1 class="slide-main-heading">AI Used <span class="highlight-red-text">Cases</span></h1>
              </div>

              <div class="usecases-list-grid">
                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Face Recognition</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">PPE Violation Detection</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">ANPR Solution</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Speed Detection System</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Silent Attendance</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Product Counting System</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Fire & Smoke Detection System</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Fall Detection Solution</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Head/People Counting Solution</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Behavior Analysis</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Perimeter Intrusion Detection</span>
                </div>

                <div class="usecase-item">
                  <div class="usecase-check-circle">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                  </div>
                  <span class="usecase-name">Forklift Automation</span>
                </div>
              </div>
            </div>

            <!-- Right Column: 12-Feed AI Vision Platform Visual -->
            <div class="usecases-right-column">
              <div class="usecases-image-frame">
                <img src="assets/ai_vision_platform_12_cases.jpg" alt="AI Vision Platform - 12 Use Cases" class="usecases-matrix-img" onerror="this.src='assets/ai_used_cases_grid.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 4,
        'tag': '04 // PROCESS ANALYTICS',
        'title': 'Standard Process Analytics',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + 6 Topics -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 12 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Standard Process <span class="highlight-red-text">Analytics</span></h1>
                <p class="analytics-desc-lead">
                  A systematic approach to analyzing workflows using data and KPIs to identify inefficiencies, optimize performance, and drive continuous improvement. It ensures consistency, transparency, and informed decision-making across operations through real-time monitoring, dashboards, and actionable insights.
                </p>
              </div>

              <!-- All 6 Solution Topics (Titles Only, No Inner Content) from PPT Slide 13 -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: AR & Ex-Proof Industrial Camera Monitoring -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path>
                      <circle cx="12" cy="13" r="4"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">AR & Ex-Proof Industrial Camera Monitoring</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 2: Thermal Imaging for Proactive Maintenance -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Thermal Imaging for Proactive Maintenance</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 3: Production Compliance & Digital Oversight -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                      <path d="m9 12 2 2 4-4"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Production Compliance & Digital Oversight</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 4: Leakage & Spillage Detection System -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Leakage & Spillage Detection System</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 5: Early Flame Detection System -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-red">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Early Flame Detection System</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 6: Real-Time Dashboards & Actionable Insights -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-slate">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                      <line x1="8" y1="21" x2="16" y2="21"></line>
                      <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Real-Time Dashboards & Actionable Insights</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

              </div>
            </div>

            <!-- Right Column: Process Analytics & Thermal AI Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/process_analytics_visual.jpg" alt="Industrial Process Analytics & Thermal AI" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 5,
        'tag': '05 // HR MANAGEMENT',
        'title': 'HR Management Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + 5 Topics -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 14 & 15 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">HR Management <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A digital system designed to streamline and automate human resource functions such as recruitment, attendance, payroll, performance tracking, and employee data management—enhancing organizational efficiency, compliance, and workforce engagement through centralized, real-time, and user-friendly tools.
                </p>
              </div>

              <!-- All 5 Solution Topics from PPT Slide 15 -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: Access Attendance Solution -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="10"></circle>
                      <polyline points="12 6 12 12 16 14"></polyline>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Access Attendance Solution</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 2: Payroll Software -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="4" width="20" height="16" rx="2"></rect>
                      <line x1="12" y1="8" x2="12" y2="16"></line>
                      <line x1="8" y1="12" x2="16" y2="12"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Payroll Software</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 3: Canteen Management Software -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>
                      <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>
                      <line x1="6" y1="1" x2="6" y2="4"></line>
                      <line x1="10" y1="1" x2="10" y2="4"></line>
                      <line x1="14" y1="1" x2="14" y2="4"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Canteen Management Software</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 4: Head Count Solution -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                      <circle cx="9" cy="7" r="4"></circle>
                      <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                      <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Head Count Solution</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 5: Visitor Management Solution -->
                <div class="analytics-topic-card card-span-2">
                  <div class="analytics-icon-box badge-red">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Visitor Management Solution</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

              </div>
            </div>

            <!-- Right Column: HRMS & Biometric Facility Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/hrms_facility_visual.jpg" alt="HRMS & Biometric Speed Gates Facility Automation" class="analytics-matrix-img" onerror="this.src='assets/cover_ai_neural_brain.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 6,
        'tag': '06 // GATE AUTOMATION',
        'title': 'Gate Automation Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + Exactly 2 Topics from PPT Slide 17 -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 16 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Gate Automation <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A smart security system that automates gate operations using sensors, remote controls, RFID, or face recognition. It enhances safety, convenience, and access control by enabling seamless, contactless entry and exit for residential, commercial, or industrial premises.
                </p>
              </div>

              <!-- Exactly the 2 Modules from PPT Slide 17 with Exact Verbatim Content -->
              <div class="gate-modules-stack">
                
                <!-- Module 1: Advanced Access & Entry Screening System -->
                <div class="gate-module-card">
                  <div class="gate-module-header">
                    <div class="analytics-icon-box badge-blue">
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="9" y1="3" x2="9" y2="21"></line>
                      </svg>
                    </div>
                    <h3 class="gate-module-title">Advanced Access & Entry Screening System</h3>
                  </div>
                  <p class="gate-module-desc">
                    A unified access solution combining face/card-based authentication with boom barriers, turnstiles, and integrated video logging. Enhanced with metal detectors, X-ray scanners, and head counting, it ensures secure, efficient, and multi-layered entry control for high-security zones.
                  </p>
                </div>

                <!-- Module 2: Electric Fence & Intelligent Perimeter Security -->
                <div class="gate-module-card">
                  <div class="gate-module-header">
                    <div class="analytics-icon-box badge-amber">
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                      </svg>
                    </div>
                    <h3 class="gate-module-title">Electric Fence & Intelligent Perimeter Security</h3>
                  </div>
                  <p class="gate-module-desc">
                    Secure your premises with advanced electric fencing designed to deter unauthorized access, detect intrusion attempts, and provide reliable 24/7 perimeter protection, enhancing safety, security, and peace of mind.
                  </p>
                </div>

              </div>
            </div>

            <!-- Right Column: Gate Automation & Perimeter Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/gate_automation_visual.jpg" alt="Gate Automation & Electric Perimeter Security" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 7,
        'tag': '07 // LIFE SAVING',
        'title': 'Life Saving Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + 4 Modules from PPT Slide 18 & 19 -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 18 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Life Saving <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A technology or system designed to prevent accidents, detect emergencies, and respond rapidly—using sensors, AI, and real-time alerts to protect lives in environments like homes, workplaces, hospitals, or public spaces, ensuring timely intervention and enhanced personal safety.
                </p>
              </div>

              <!-- 4 Strategic Module Headings -->
              <div class="analytics-cards-grid">
                
                <!-- Module 1: Fire Detection System -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-red">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Fire Detection System</h3>
                </div>

                <!-- Module 2: Fire Suppression Solutions -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                      <path d="m9 12 2 2 4-4"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Fire Suppression Solutions</h3>
                </div>

                <!-- Module 3: PPE & Compliance -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                      <circle cx="12" cy="11" r="3"></circle>
                      <path d="M7 18.5a5 5 0 0 1 10 0"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">PPE & Compliance</h3>
                </div>

                <!-- Module 4: Smart Home Guarding -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                      <polyline points="9 22 9 12 15 12 15 22"></polyline>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Smart Home Guarding</h3>
                </div>

              </div>
            </div>

            <!-- Right Column: Life Saving & Safety Telemetry Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/life_saving_visual.jpg" alt="Life Saving Solution, Fire Detection & PPE Telemetry" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 8,
        'tag': '08 // BUILDING MANAGEMENT',
        'title': 'Building Management Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + 4 Modules from PPT Slide 20 & 21 -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 20 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Building Management <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  An integrated system that monitors and controls a building's electrical, mechanical, and safety infrastructure. It enhances energy efficiency, comfort, and security through automation, real-time data, and centralized control of lighting, HVAC, access, fire systems, and other facility operations.
                </p>
              </div>

              <!-- 4 Strategic Module Headings -->
              <div class="analytics-cards-grid">
                
                <!-- Module 1: Building Management Solution (BMS) -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect>
                      <line x1="9" y1="22" x2="9" y2="22.01"></line>
                      <line x1="15" y1="22" x2="15" y2="22.01"></line>
                      <line x1="8" y1="6" x2="8" y2="6.01"></line>
                      <line x1="12" y1="6" x2="12" y2="6.01"></line>
                      <line x1="16" y1="6" x2="16" y2="6.01"></line>
                      <line x1="8" y1="10" x2="8" y2="10.01"></line>
                      <line x1="12" y1="10" x2="12" y2="10.01"></line>
                      <line x1="16" y1="10" x2="16" y2="10.01"></line>
                      <line x1="8" y1="14" x2="8" y2="14.01"></line>
                      <line x1="12" y1="14" x2="12" y2="14.01"></line>
                      <line x1="16" y1="14" x2="16" y2="14.01"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Building Management Solution (BMS)</h3>
                </div>

                <!-- Module 2: DDC Controllers -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="4" y="4" width="16" height="16" rx="2"></rect>
                      <rect x="9" y="9" width="6" height="6"></rect>
                      <line x1="9" y1="1" x2="9" y2="4"></line>
                      <line x1="15" y1="1" x2="15" y2="4"></line>
                      <line x1="9" y1="20" x2="9" y2="23"></line>
                      <line x1="15" y1="20" x2="15" y2="23"></line>
                      <line x1="20" y1="9" x2="23" y2="9"></line>
                      <line x1="20" y1="14" x2="23" y2="14"></line>
                      <line x1="1" y1="9" x2="4" y2="9"></line>
                      <line x1="1" y1="14" x2="4" y2="14"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">DDC Controllers</h3>
                </div>

                <!-- Module 3: Field Devices -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="3"></circle>
                      <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Field Devices</h3>
                </div>

                <!-- Module 4: Smart Building -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Smart Building</h3>
                </div>

              </div>
            </div>

            <!-- Right Column: BMS & Smart Building Architecture Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/bms_smart_building_visual.jpg" alt="Building Management Solution BMS Smart Building IoT" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 9,
        'tag': '09 // DIGITAL SOLUTION',
        'title': 'Digital Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + Integrated IT Infrastructure -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 22 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Digital <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A technology-driven approach that leverages software, cloud, AI, or automation to solve business challenges, improve efficiency, enhance customer experience, and enable innovation. It transforms traditional processes into streamlined, scalable, and intelligent systems across various industries and functions.
                </p>
              </div>

              <!-- 4 Strategic Module Headings -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: Advanced Networking & Cybersecurity -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                      <path d="m9 12 2 2 4-4"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Advanced Networking &amp; Cybersecurity</h3>
                </div>

                <!-- Topic 2: Wireless Communication -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M5 12.55a11 11 0 0 1 14.08 0"></path>
                      <path d="M1.42 9a16 16 0 0 1 21.16 0"></path>
                      <path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path>
                      <line x1="12" y1="20" x2="12.01" y2="20"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Wireless Communication</h3>
                </div>

                <!-- Topic 3: Smart Racks & Data Center -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect>
                      <rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect>
                      <line x1="6" y1="6" x2="6.01" y2="6"></line>
                      <line x1="6" y1="18" x2="6.01" y2="18"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Smart Racks &amp; Data Center</h3>
                </div>

                <!-- Topic 4: Servers & IT Infrastructure -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="4" y="4" width="16" height="16" rx="2"></rect>
                      <rect x="9" y="9" width="6" height="6"></rect>
                      <line x1="9" y1="1" x2="9" y2="4"></line>
                      <line x1="15" y1="1" x2="15" y2="4"></line>
                      <line x1="9" y1="20" x2="9" y2="23"></line>
                      <line x1="15" y1="20" x2="15" y2="23"></line>
                      <line x1="20" y1="9" x2="23" y2="9"></line>
                      <line x1="20" y1="14" x2="23" y2="14"></line>
                      <line x1="1" y1="9" x2="4" y2="9"></line>
                      <line x1="1" y1="14" x2="4" y2="14"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Servers &amp; IT Infrastructure</h3>
                </div>

              </div>
            </div>

            <!-- Right Column: Digital Infrastructure & Cyber Control Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/digital_solution_visual.jpg" alt="Integrated IT Infrastructure and Cybersecurity" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 10,
        'tag': '10 // EDUCATION SOLUTION',
        'title': 'Education Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + 5 Topics from PPT Slide 24 & 25 -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 24 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Education <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A smart system using digital tools, AI, and automation to enhance teaching, learning, and administration. It supports virtual classrooms, student tracking, content delivery, and performance analysis—improving engagement, accessibility, and efficiency in schools, colleges, and training institutions.
                </p>
              </div>

              <!-- 4 Strategic Module Headings (Titles Only) -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: Classroom Monitoring System -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path>
                      <circle cx="12" cy="13" r="4"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Classroom Monitoring System</h3>
                </div>

                <!-- Topic 2: Broadcasting Solution -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"></path>
                      <path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"></path>
                      <circle cx="12" cy="12" r="2"></circle>
                      <path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"></path>
                      <path d="M19.1 4.9C23 8.8 23 15.2 19.1 19.1"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Broadcasting Solution</h3>
                </div>

                <!-- Topic 3: Attendance & Access Control -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                      <circle cx="12" cy="10" r="3"></circle>
                      <path d="M7 17.5a5 5 0 0 1 10 0"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Attendance &amp; Access Control</h3>
                </div>

                <!-- Topic 4: Interactive Display -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="3" width="20" height="14" rx="2"></rect>
                      <line x1="8" y1="21" x2="16" y2="21"></line>
                      <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Interactive Display</h3>
                </div>

              </div>
            </div>

            <!-- Right Column: Smart Education Campus Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/smart_education_visual.jpg" alt="Smart Education Campus Classroom AI and Telemetry" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 11,
        'tag': '11 // MOBILE SURVEILLANCE',
        'title': 'Mobile Surveillance Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + MSS Module & Key Benefits -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 26 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Mobile Surveillance <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A portable security system using cameras, wireless connectivity, and real-time monitoring to track and record activities in remote or moving locations. Ideal for events, construction sites, and law enforcement, it ensures flexible, on-the-go surveillance and rapid incident response.
                </p>
              </div>

              <!-- 4 Strategic Module Headings -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: Mobile Surveillance Vehicle (MSV) -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="1" y="3" width="15" height="13"></rect>
                      <polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon>
                      <circle cx="5.5" cy="18.5" r="2.5"></circle>
                      <circle cx="18.5" cy="18.5" r="2.5"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Mobile Surveillance Vehicle (MSV)</h3>
                </div>

                <!-- Topic 2: Real-Time Transport Monitoring -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="3" width="20" height="14" rx="2"></rect>
                      <line x1="8" y1="21" x2="16" y2="21"></line>
                      <line x1="12" y1="17" x2="12" y2="21"></line>
                      <path d="M6 8h.01M10 8h.01M14 8h.01M18 8h.01"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Real-Time Transport Monitoring</h3>
                </div>

                <!-- Topic 3: GPS Tracking & Fleet Management -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <polygon points="12 2 19 21 12 17 5 21 12 2"></polygon>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">GPS Tracking &amp; Fleet Management</h3>
                </div>

                <!-- Topic 4: Video Analytics & Safety Alerts -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                      <path d="m9 12 2 2 4-4"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Video Analytics &amp; Safety Alerts</h3>
                </div>

              </div>
            </div>

            <!-- Right Column: Mobile Surveillance & Trailer Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/mobile_surveillance_visual.jpg" alt="Mobile Surveillance Solution MSS and Rapid Deployment Unit" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 12,
        'tag': '12 // TRAFFIC MANAGEMENT',
        'title': 'Traffic Management Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + Smart Traffic & Vehicle Tracking Solution -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 28 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Traffic Management <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  An intelligent system that uses sensors, cameras, and AI to monitor, analyze, and control traffic flow. It reduces congestion, enhances road safety, and optimizes signal timing—supporting smart city infrastructure and efficient transportation through real-time data and automation.
                </p>
              </div>

              <!-- 4 Strategic Module Headings -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: Smart Traffic & Vehicle Tracking -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <polygon points="12 2 19 21 12 17 5 21 12 2"></polygon>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Smart Traffic &amp; Vehicle Tracking</h3>
                </div>

                <!-- Topic 2: Traffic Surveillance & Incident Detection -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path>
                      <circle cx="12" cy="13" r="4"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Traffic Surveillance &amp; Incident Detection</h3>
                </div>

                <!-- Topic 3: Intelligent Traffic Control & Communication -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="6" y="2" width="12" height="20" rx="4"></rect>
                      <circle cx="12" cy="6" r="1.5" fill="currentColor"></circle>
                      <circle cx="12" cy="12" r="1.5" fill="currentColor"></circle>
                      <circle cx="12" cy="18" r="1.5" fill="currentColor"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Intelligent Traffic Control &amp; Communication</h3>
                </div>

                <!-- Topic 4: Traffic Analytics & Command Center -->
                <div class="analytics-topic-card">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M2 12h5l3 7 4-14 3 7h5"></path>
                      <circle cx="12" cy="12" r="1"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Traffic Analytics &amp; Command Center</h3>
                </div>

              </div>
            </div>

            <!-- Right Column: Smart Traffic & Vehicle Tracking Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/traffic_management_visual.jpg" alt="Smart Traffic and GPS Vehicle Tracking System" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 13,
        'tag': '13 // PARKING MANAGEMENT',
        'title': 'Parking Management Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + Smart Parking Security & Core Features -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 30 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Parking Management <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A smart system that automates vehicle entry, exit, and space allocation using sensors, cameras, and software. It improves space utilization, reduces congestion, enables digital payments, and provides real-time availability updates—enhancing convenience and efficiency in public and private parking areas.
                </p>
              </div>

              <!-- 3 Strategic Module Headings -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: ANPR Camera Systems -->
                <div class="analytics-topic-card card-span-2">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="5" width="20" height="14" rx="2"></rect>
                      <circle cx="12" cy="12" r="3.5"></circle>
                      <path d="M19 8h.01"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">ANPR Camera Systems</h3>
                </div>

                <!-- Topic 2: Automatic Barrier Systems -->
                <div class="analytics-topic-card card-span-2">
                  <div class="analytics-icon-box badge-amber">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="3" y="11" width="4" height="10" rx="1"></rect>
                      <path d="M7 13l14-5"></path>
                      <circle cx="5" cy="13" r="1.5"></circle>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Automatic Barrier Systems</h3>
                </div>

                <!-- Topic 3: Radar Detection Technology -->
                <div class="analytics-topic-card card-span-2">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 20a8 8 0 1 0 0-16 8 8 0 0 0 0 16z"></path>
                      <path d="M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"></path>
                      <path d="M12 2v2M12 20v2M2 12h2M20 12h2"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Radar Detection Technology</h3>
                </div>

              </div>
            </div>

            <!-- Right Column: Parking Structure & ANPR Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/parking_management_visual.jpg" alt="Smart Parking Multi-Level Structure and ANPR Camera System" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 14,
        'tag': '14 // HOSPITALITY SOLUTION',
        'title': 'Hospitality Solution',
        'type': 'content',
        'html': '''
          <div class="slide-analytics-split-layout">
            <!-- Left Column: Header + 3 Topic Cards (Titles Only) from PPT Slide 32 & 33 -->
            <div class="analytics-left-column">
              <!-- Header Section with Exact Definition from PPT Slide 32 -->
              <div class="analytics-header-block">
                <h1 class="slide-main-heading">Hospitality <span class="highlight-red-text">Solution</span></h1>
                <p class="analytics-desc-lead">
                  A comprehensive system designed to enhance guest experience and streamline hotel operations using automation, IoT, and digital tools. It manages bookings, check-ins, room controls, and services—improving efficiency, personalization, and satisfaction in hotels, resorts, and other hospitality environments.
                </p>
              </div>

              <!-- All 3 Solution Topics (Titles Only, No Inner Paragraphs) from PPT Slide 33 -->
              <div class="analytics-cards-grid">
                
                <!-- Topic 1: Nurse/Attendant Calling System -->
                <div class="analytics-topic-card card-span-2">
                  <div class="analytics-icon-box badge-blue">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                      <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Nurse/Attendant Calling System</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 2: Unified Communications Platform -->
                <div class="analytics-topic-card card-span-2">
                  <div class="analytics-icon-box badge-purple">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="2" y="2" width="20" height="8" rx="2"></rect>
                      <rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect>
                      <line x1="6" y1="6" x2="6.01" y2="6"></line>
                      <line x1="6" y1="18" x2="6.01" y2="18"></line>
                      <path d="M12 10v4"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Unified Communications Platform</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

                <!-- Topic 3: Finger/Card Lock System -->
                <div class="analytics-topic-card card-span-2">
                  <div class="analytics-icon-box badge-emerald">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                      <rect x="3" y="11" width="18" height="11" rx="2"></rect>
                      <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                    </svg>
                  </div>
                  <h3 class="analytics-card-title">Finger/Card Lock System</h3>
                  <div class="analytics-card-arrow">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
                  </div>
                </div>

              </div>
            </div>

            <!-- Right Column: Hospitality & Smart Facility Visual Frame -->
            <div class="analytics-right-column">
              <div class="analytics-image-frame">
                <img src="assets/hospitality_solution_visual.jpg" alt="Smart Facility Communication and Access Systems" class="analytics-matrix-img" onerror="this.src='assets/cover_diamond_surveillance.jpg'" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 15,
        'tag': '15 // PRESTIGIOUS CLIENTS',
        'title': 'Our Few Prestigious Clients',
        'type': 'content',
        'html': f'''
          <div class="slide-clients-showcase-layout">
            <!-- Clean Header (Only Heading) -->
            <div class="clients-header-block">
              <h1 class="slide-main-heading">Our Few <span class="highlight-red-text">Prestigious Clients</span></h1>
            </div>

            <!-- Single Unified Showcase Stage with Responsive Logo Grid -->
            <div class="clients-showcase-stage">
              <div class="clients-grid-scroll-box">
                <div class="clients-alphabetical-grid">
{client_cards_html}
                </div>
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 16,
        'tag': '16 // NIMIT ECO SYSTEM',
        'title': 'NIMIT Eco System',
        'type': 'content',
        'html': '''
          <div class="slide-sectors-ecosystem-layout">
            <!-- Header Section with NIMIT Eco System Heading -->
            <div class="sectors-header-block">
              <h1 class="slide-main-heading">NIMIT <span class="highlight-red-text">Eco System</span></h1>
            </div>

            <!-- 9 Sectors Matrix in 2 Balanced Rows (4 on Top, 5 on Bottom) matching PPT Slide 36 -->
            <div class="sectors-matrix-container">
              <!-- Top Row: 4 Sectors -->
              <div class="sectors-row-4">
                <!-- 1. Industries -->
                <div class="sector-card-box theme-red">
                  <div class="sector-icon-stage">
                    <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M2 20h20M6 20V10l6 4V4l8 6v10M18 14h.01M18 17h.01M14 17h.01M10 17h.01"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Industries</span>
                </div>

                <!-- 2. Religious Place -->
                <div class="sector-card-box theme-amber">
                  <div class="sector-icon-stage">
                    <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 2l3 5h-6l3-5zM9 7h6v5H9zM4 12h16v8H4zM12 12v8M8 20v-4h8v4"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Religious Place</span>
                </div>

                <!-- 3. Education -->
                <div class="sector-card-box theme-blue">
                  <div class="sector-icon-stage">
                    <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 3 6 3 6 3s6 0 6-3v-5"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Education</span>
                </div>

                <!-- 4. Hotel & Restaurant -->
                <div class="sector-card-box theme-purple">
                  <div class="sector-icon-stage">
                    <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 9h1M14 9h1M9 13h1M14 13h1M9 17h1M14 17h1"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Hotel & Restaurant</span>
                </div>
              </div>

              <!-- Bottom Row: 5 Sectors -->
              <div class="sectors-row-5">
                <!-- 5. Campus -->
                <div class="sector-card-box theme-cyan">
                  <div class="sector-icon-stage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M2 22h20M12 2l8 4.5V22H4V6.5zM12 11h.01M12 15h.01M8 11h.01M8 15h.01M16 11h.01M16 15h.01"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Campus</span>
                </div>

                <!-- 6. Showroom -->
                <div class="sector-card-box theme-emerald">
                  <div class="sector-icon-stage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/><path d="M7 9h10"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Showroom</span>
                </div>

                <!-- 7. Jewellers -->
                <div class="sector-card-box theme-pink">
                  <div class="sector-icon-stage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M6 3h12l4 6-10 12L2 9z"/><polyline points="11 3 8 9 2 9"/><polyline points="13 3 16 9 22 9"/><polyline points="8 9 12 21 16 9"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Jewellers</span>
                </div>

                <!-- 8. Hospital -->
                <div class="sector-card-box theme-red">
                  <div class="sector-icon-stage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/><path d="M12 7v6M9 10h6"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Hospital</span>
                </div>

                <!-- 9. Government Sector -->
                <div class="sector-card-box theme-slate">
                  <div class="sector-icon-stage">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M2 20h20M4 20V9M8 20V9M12 20V9M16 20V9M20 20V9M2 9l10-6 10 6M2 22h20"/>
                    </svg>
                  </div>
                  <span class="sector-card-title">Government Sector</span>
                </div>
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 17,
        'tag': '17 // OUR PEOPLE',
        'title': 'Core Team',
        'type': 'content',
        'html': '''
          <div class="slide-core-team-layout">
            <!-- Header Section with Heading CORE TEAM -->
            <div class="core-team-header-block">
              <h1 class="slide-main-heading">CORE <span class="highlight-red-text">TEAM</span></h1>
            </div>

            <!-- Central Showcase Stage with Team Photo -->
            <div class="core-team-showcase-stage">
              <div class="core-team-img-wrapper">
                <img src="assets/nimit_core_team.png" alt="NIMIT Core Team" class="core-team-photo" />
              </div>
            </div>
          </div>
        '''
    },
    {
        'num': 18,
        'tag': '18 // CONTACT',
        'title': 'Contact Us & Headquarters',
        'type': 'content',
        'html': '''
          <div class="slide-contact-clean-layout">
            <!-- Clean Header Block -->
            <div class="clean-contact-header">
              <h1 class="slide-main-heading">CONTACT US</h1>
              <p class="slide-sub-heading">Partner with Nimit AI for intelligent, scalable vision surveillance solutions</p>
            </div>

            <div class="clean-contact-grid">
              <a href="https://www.google.com/maps/place/Nimit+Electronics+And+Equipment/@22.2541064,73.1770643,17z/data=!4m14!1m7!3m6!1s0x395fc58df93df51b:0x8156a02152f176f2!2sNimit+Electronics+And+Equipment!8m2!3d22.2541015!4d73.1796392!16s%2Fg%2F11h2mcb2qr!3m5!1s0x395fc58df93df51b:0x8156a02152f176f2!8m2!3d22.2541015!4d73.1796392!16s%2Fg%2F11h2mcb2qr?entry=ttu&g_ep=EgoyMDI2MDkxNS4wIKXMDSoASAFQAw%3D%3D" target="_blank" rel="noopener noreferrer" class="clean-contact-card">
                <div class="clean-contact-icon-circle icon-circle-red">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                </div>
                <div class="clean-contact-info">
                  <span class="clean-contact-label">HEAD OFFICE</span>
                  <span class="clean-contact-val hq-addr-val">457, GIDC Makarpura, Vadodara</span>
                  <span class="clean-contact-sub">Gujarat-390010, India (View on Map ↗)</span>
                </div>
              </a>

              <div class="clean-contact-card" style="cursor:default;">
                <div class="clean-contact-icon-circle icon-circle-blue">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/>
                    <path d="M2 12h20"/>
                  </svg>
                </div>
                <div class="clean-contact-info">
                  <span class="clean-contact-label" style="color:var(--primary-red); font-weight:800;">OUR PRESENCE</span>
                  <span class="clean-contact-val" style="font-size:clamp(0.8rem, 0.98vw, 1.02rem); font-weight:700; line-height:1.4; color:var(--slate-dark);">
                    Surat, Ahmedabad, Jamnagar, Kutch, Indore, Delhi, Mumbai, Bangalore, Patna, Hyderabad, Dehradun, Kanpur
                  </span>
                  <span class="clean-contact-sub">Pan-India Deployment & Technical Support</span>
                </div>
              </div>

              <a href="https://wa.me/919824093685" target="_blank" rel="noopener noreferrer" class="clean-contact-card">
                <div class="clean-contact-icon-circle icon-circle-green">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                </div>
                <div class="clean-contact-info">
                  <span class="clean-contact-label">PHONE & WHATSAPP</span>
                  <span class="clean-contact-val" style="font-size:clamp(1rem, 1.3vw, 1.4rem);">+91 98240 93685</span>
                  <span class="clean-contact-sub">+91 99242 98685 &nbsp;|&nbsp; +91 99251 48685</span>
                </div>
              </a>

              <a href="https://www.nimitelectronics.com" target="_blank" rel="noopener noreferrer" class="clean-contact-card">
                <div class="clean-contact-icon-circle icon-circle-red">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <rect width="20" height="16" x="2" y="4" rx="2"/>
                    <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
                  </svg>
                </div>
                <div class="clean-contact-info">
                  <span class="clean-contact-label">EMAIL & OFFICIAL PORTAL</span>
                  <span class="clean-contact-val" style="font-size:clamp(0.92rem, 1.2vw, 1.28rem);">info@nimitelectronics.com</span>
                  <span class="clean-contact-sub">www.nimitelectronics.com ↗</span>
                </div>
              </a>
            </div>
          </div>
        '''
    }
]

slides_json_str = json.dumps(slides_data, indent=2)
total_count = len(slides_data)

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>NIMIT AI — Industry Solutions</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,700&family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600;700;800&display=swap" rel="stylesheet" />

  <style>
    :root {{
      --primary-red: #e51924;
      --primary-red-hover: #cc151f;
      --primary-red-glow: rgba(229, 25, 36, 0.35);
      --burgundy: #8B0000;
      --charcoal: #0f172a;
      --slate-dark: #1e293b;
      --slate-muted: #475569;
      --slate-light: #64748b;
      --border-card: #e2e8f0;
      --bg-stage: #f8fafc;
      --font-display: 'Plus Jakarta Sans', 'Outfit', sans-serif;
      --font-heading: 'Space Grotesk', sans-serif;
      --font-body: 'Inter', sans-serif;
      --font-mono: 'JetBrains Mono', 'Space Grotesk', monospace;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    html, body {{
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      overflow: hidden;
      background: #f8fafc;
      font-family: var(--font-display);
      color: var(--charcoal);
      user-select: none;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* Top Reading Progress Bar */
    .slide-progress-tracker {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: rgba(0, 0, 0, 0.06);
      z-index: 999;
    }}

    .slide-progress-fill {{
      height: 100%;
      width: 12.5%;
      background: linear-gradient(90deg, #1e293b, #e51924);
      transition: width 0.3s ease;
    }}

    /* Master Screen Canvas Container */
    .app-screen-canvas {{
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: background 0.35s ease;
    }}

    /* State 1: Cover Slide background */
    .app-screen-canvas.is-cover-slide {{
      background: radial-gradient(ellipse at 20% 45%, rgba(254, 226, 226, 0.6) 0%, rgba(255, 255, 255, 0.95) 45%, #f8fafc 100%);
    }}

    /* State 2: Content Slides (Pure White / Soft Stage) */
    .app-screen-canvas.is-content-slide {{
      background: #ffffff;
    }}

    /* 60fps Neural Particle Canvas (visible on cover, subtle on content) */
    #neuralCanvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: auto;
      z-index: 2;
      opacity: 0.85;
      transition: opacity 0.3s ease;
    }}

    .is-content-slide #neuralCanvas {{
      opacity: 0.12;
      pointer-events: none;
    }}

    /* Geometric Soft Tint Shapes for Cover Slide Background */
    .cover-bg-polygon-top {{
      position: absolute;
      top: 0;
      left: 0;
      width: 45vw;
      height: 45vh;
      background: linear-gradient(135deg, rgba(229, 25, 36, 0.035) 0%, rgba(229, 25, 36, 0.005) 100%);
      clip-path: polygon(0 0, 100% 0, 0 100%);
      z-index: 1;
      pointer-events: none;
    }}

    .cover-bg-polygon-right {{
      position: absolute;
      top: 0;
      right: 0;
      width: 35vw;
      height: 35vh;
      background: linear-gradient(225deg, rgba(30, 41, 59, 0.03) 0%, rgba(30, 41, 59, 0.002) 100%);
      clip-path: polygon(100% 0, 100% 100%, 0 0);
      z-index: 1;
      pointer-events: none;
    }}

    .is-content-slide .cover-bg-polygon-top,
    .is-content-slide .cover-bg-polygon-right {{
      display: none;
    }}

    /* Main Foreground Layout */
    .foreground-content {{
      position: relative;
      z-index: 10;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: clamp(0.6rem, 1.4vh, 1.2rem) clamp(1.2rem, 3.2vw, 3.6rem) clamp(58px, 8vh, 72px) clamp(1.2rem, 3.2vw, 3.6rem);
      pointer-events: none;
    }}

    .foreground-content * {{
      pointer-events: auto;
    }}

    /* =====================================================
       1. TOP HEADER ROW
       ===================================================== */
    .header-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      flex-shrink: 0;
    }}

    .brand-logo-block {{
      display: flex;
      flex-direction: column;
      cursor: pointer;
    }}

    .logo-img {{
      width: clamp(180px, 18vw, 290px);
      height: auto;
      display: block;
      object-fit: contain;
      filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.08));
      transition: transform 0.25s ease;
    }}

    .logo-img:hover {{
      transform: scale(1.02);
    }}

    .brand-tagline {{
      font-size: clamp(0.65rem, 0.78vw, 0.85rem);
      font-weight: 700;
      letter-spacing: 0.22em;
      color: #334155;
      margin-top: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }}

    .brand-tagline span {{
      color: var(--primary-red);
      font-weight: 900;
    }}

    /* Portal Navigation Bar (Aesthetic Floating Glass Pill) */
    .portal-nav-bar {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      padding: 0.24rem 0.32rem;
      border-radius: 9999px;
      border: 1px solid rgba(226, 232, 240, 0.95);
      box-shadow: 0 4px 18px -2px rgba(15, 23, 42, 0.07), 0 2px 6px -1px rgba(15, 23, 42, 0.04);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .portal-nav-bar:hover {{
      background: #ffffff;
      border-color: rgba(203, 213, 225, 1);
      box-shadow: 0 6px 22px -2px rgba(15, 23, 42, 0.11);
    }}

    .portal-nav-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      font-family: var(--font-display, 'Outfit', sans-serif);
      font-size: 0.78rem;
      font-weight: 700;
      color: #334155;
      text-decoration: none;
      padding: 0.32rem 0.85rem 0.32rem 0.4rem;
      border-radius: 9999px;
      border: 1px solid transparent;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      letter-spacing: -0.01em;
    }}

    .portal-nav-link .nav-icon-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #f1f5f9;
      color: #64748b;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      flex-shrink: 0;
    }}

    .portal-nav-link .nav-icon-badge svg {{
      transition: transform 0.22s ease;
    }}

    .portal-nav-link:hover {{
      color: var(--primary-red);
      background: rgba(229, 25, 36, 0.06);
      border-color: rgba(229, 25, 36, 0.18);
      transform: translateY(-1px);
    }}

    .portal-nav-link:hover .nav-icon-badge {{
      background: linear-gradient(135deg, #e51924 0%, #b9131c 100%);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(229, 25, 36, 0.35);
      transform: scale(1.08);
    }}

    .portal-nav-link:hover .nav-icon-badge svg {{
      transform: scale(1.1);
    }}

    .portal-nav-link.active {{
      background: linear-gradient(135deg, #e51924 0%, #b9131c 100%);
      color: #ffffff;
      border-color: transparent;
      box-shadow: 0 3px 12px rgba(229, 25, 36, 0.32);
    }}

    .portal-nav-link.active .nav-icon-badge {{
      background: rgba(255, 255, 255, 0.22);
      color: #ffffff;
      box-shadow: none;
    }}

    .header-right-tools {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .btn-toc-drawer {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.45rem 0.85rem;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(226, 232, 240, 0.9);
      border-radius: 8px;
      font-family: var(--font-display);
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--charcoal);
      cursor: pointer;
      backdrop-filter: blur(8px);
      transition: all 0.2s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }}

    .btn-toc-drawer:hover {{
      background: #ffffff;
      border-color: var(--primary-red);
      color: var(--primary-red);
      transform: translateY(-1px);
    }}

    /* =====================================================
       2. MIDDLE STAGE VIEWPORT
       ===================================================== */
    .slide-stage-viewport {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
      height: 100%;
      margin-top: auto;
      margin-bottom: auto;
      position: relative;
      overflow: hidden;
    }}

    .slide-page-container {{
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1), transform 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .slide-page-container.fade-out {{
      opacity: 0;
      transform: scale(0.985);
    }}

    /* Manifesto Slide 1 Layout */
    .slide-manifesto-layout {{
      width: 100%;
      max-width: 980px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }}

    .manifesto-card-stage {{
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 24px;
      padding: clamp(2.8rem, 6.5vh, 5.2rem) clamp(2rem, 4vw, 5rem);
      box-shadow: 0 18px 45px rgba(0, 0, 0, 0.06);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 100%;
    }}

    .manifesto-headline-box {{
      margin: 0;
      position: relative;
    }}

    .vision-title-text {{
      font-family: var(--font-heading);
      font-size: clamp(1.9rem, 3.4vw, 3.6rem);
      font-weight: 800;
      color: var(--charcoal);
      letter-spacing: -0.03em;
      line-height: 1.1;
    }}

    .highlight-red-text {{
      color: var(--primary-red);
    }}

    .manifesto-accent-line {{
      width: 90px;
      height: 4px;
      background: linear-gradient(90deg, var(--primary-red) 0%, var(--burgundy) 100%);
      border-radius: 2px;
      margin: 0.9rem auto 0 auto;
    }}

    .manifesto-values-strip {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: clamp(0.4rem, 1vw, 0.85rem);
      flex-wrap: wrap;
      margin-top: 1.2rem;
    }}

    .manifesto-val-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.35rem 0.9rem;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 9999px;
      font-family: var(--font-display);
      font-size: clamp(0.76rem, 0.9vw, 0.92rem);
      font-weight: 700;
      color: var(--slate-dark);
    }}

    .val-pill-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
    }}
    .dot-red {{ background: var(--primary-red); }}
    .dot-burgundy {{ background: var(--burgundy); }}
    .dot-charcoal {{ background: var(--charcoal); }}

    /* =====================================================
       SMART PREMISES ALL-IN-ONE TOPICS PAGE (SLIDE 02)
       ===================================================== */
    .slide-premises-full-layout {{
      width: 100%;
      max-width: 1220px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: clamp(1rem, 2.2vh, 1.8rem);
      justify-content: center;
      height: 100%;
    }}

    .premises-header-block {{
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.35rem;
    }}

    .premises-desc-lead {{
      font-size: clamp(0.88rem, 1.05vw, 1.08rem);
      color: var(--slate-muted);
      line-height: 1.6;
      font-weight: 500;
      max-width: 960px;
      margin-top: 0.2rem;
    }}

    .premises-topics-grid-6 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: clamp(0.85rem, 1.5vw, 1.4rem);
      width: 100%;
      margin-top: 0.3rem;
    }}

    .premise-topic-card {{
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 16px;
      padding: clamp(1.1rem, 1.6vw, 1.6rem) clamp(1.1rem, 1.6vw, 1.6rem);
      display: flex;
      align-items: center;
      gap: clamp(0.85rem, 1.2vw, 1.25rem);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.035);
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      text-align: left;
      position: relative;
    }}

    .premise-topic-card:hover {{
      border-color: var(--primary-red);
      transform: translateY(-3px);
      box-shadow: 0 14px 32px rgba(229, 25, 36, 0.09);
    }}

    .premise-card-icon-box {{
      width: clamp(48px, 3.8vw, 56px);
      height: clamp(48px, 3.8vw, 56px);
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: transform 0.2s ease;
    }}

    .premise-topic-card:hover .premise-card-icon-box {{
      transform: scale(1.08);
    }}

    .badge-blue {{
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.12), rgba(56, 189, 248, 0.18));
      color: #0284c7;
      border: 1px solid rgba(2, 132, 199, 0.28);
    }}

    .badge-emerald {{
      background: linear-gradient(135deg, rgba(5, 150, 105, 0.12), rgba(52, 211, 153, 0.18));
      color: #059669;
      border: 1px solid rgba(5, 150, 105, 0.28);
    }}

    .badge-purple {{
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.18));
      color: #7c3aed;
      border: 1px solid rgba(124, 58, 237, 0.28);
    }}

    .badge-red {{
      background: linear-gradient(135deg, rgba(229, 25, 36, 0.12), rgba(248, 113, 113, 0.18));
      color: var(--primary-red);
      border: 1px solid rgba(229, 25, 36, 0.28);
    }}

    .badge-amber {{
      background: linear-gradient(135deg, rgba(217, 119, 6, 0.12), rgba(251, 191, 36, 0.18));
      color: #d97706;
      border: 1px solid rgba(217, 119, 6, 0.28);
    }}

    .badge-slate {{
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.1), rgba(71, 85, 105, 0.15));
      color: var(--charcoal);
      border: 1px solid rgba(30, 41, 59, 0.25);
    }}

    .premise-card-content {{
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      min-width: 0;
      flex-grow: 1;
    }}

    .premise-card-title {{
      font-family: var(--font-display);
      font-size: clamp(0.98rem, 1.2vw, 1.28rem);
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.25;
    }}

    .premise-card-arrow {{
      color: #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }}

    .premise-topic-card:hover .premise-card-arrow {{
      color: var(--primary-red);
      transform: translateX(3px);
    }}

    /* =====================================================
       AI USED CASES SPLIT LAYOUT (SLIDE 03)
       ===================================================== */
    .slide-usecases-split-layout {{
      width: 100%;
      max-width: 1260px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 0.98fr 1.02fr;
      gap: clamp(1.2rem, 2.5vw, 2.6rem);
      align-items: center;
      height: 100%;
    }}

    .usecases-left-column {{
      display: flex;
      flex-direction: column;
      gap: clamp(0.75rem, 1.4vh, 1.25rem);
      text-align: left;
    }}

    .usecases-header-block {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 0.25rem;
    }}

    .usecases-list-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: clamp(0.45rem, 0.85vw, 0.72rem) clamp(0.6rem, 1.2vw, 1.1rem);
      width: 100%;
    }}

    .usecase-item {{
      display: flex;
      align-items: center;
      gap: clamp(0.5rem, 0.75vw, 0.75rem);
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 10px;
      padding: clamp(0.48rem, 0.75vw, 0.7rem) clamp(0.65rem, 0.95vw, 0.9rem);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .usecase-item:hover {{
      border-color: var(--primary-red);
      transform: translateX(3px);
      box-shadow: 0 4px 14px rgba(229, 25, 36, 0.08);
    }}

    .usecase-check-circle {{
      width: clamp(24px, 1.8vw, 28px);
      height: clamp(24px, 1.8vw, 28px);
      border-radius: 50%;
      background: rgba(229, 25, 36, 0.08);
      color: var(--primary-red);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .usecase-name {{
      font-family: var(--font-display);
      font-size: clamp(0.82rem, 0.94vw, 1rem);
      font-weight: 700;
      color: var(--slate-dark);
      line-height: 1.25;
    }}

    .usecases-right-column {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      width: 100%;
    }}

    .usecases-image-frame {{
      position: relative;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      background: #0f172a;
    }}

    .usecases-matrix-img {{
      width: 100%;
      height: auto;
      aspect-ratio: 1024 / 573;
      object-fit: contain;
      display: block;
      transition: transform 0.3s ease;
    }}

    .usecases-matrix-img:hover {{
      transform: scale(1.015);
    }}

    .usecases-image-overlay-badge {{
      position: absolute;
      bottom: 0.75rem;
      left: 0.75rem;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 9999px;
      padding: 0.28rem 0.75rem;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.1em;
    }}

    .matrix-live-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
    }}

    /* =====================================================
       PROCESS ANALYTICS SPLIT LAYOUT (SLIDE 04)
       ===================================================== */
    .slide-analytics-split-layout {{
      width: 100%;
      max-width: 1260px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: clamp(1.2rem, 2.2vw, 2.4rem);
      align-items: center;
      height: 100%;
    }}

    .analytics-left-column {{
      display: flex;
      flex-direction: column;
      gap: clamp(0.5rem, 1vh, 0.9rem);
      text-align: left;
    }}

    .analytics-header-block {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 0.25rem;
    }}

    .analytics-desc-lead {{
      font-size: clamp(0.76rem, 0.92vw, 0.92rem);
      color: #475569;
      line-height: 1.5;
      font-weight: 500;
      margin-top: 0.25rem;
    }}

    .analytics-cards-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: clamp(0.45rem, 0.75vw, 0.7rem);
      width: 100%;
    }}

    .analytics-topic-card {{
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 12px;
      padding: clamp(0.55rem, 0.8vw, 0.8rem) clamp(0.65rem, 1vw, 0.95rem);
      display: flex;
      align-items: center;
      gap: clamp(0.55rem, 0.8vw, 0.8rem);
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      text-align: left;
      position: relative;
    }}

    .analytics-topic-card:hover {{
      border-color: var(--primary-red);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(229, 25, 36, 0.09);
    }}

    .analytics-icon-box {{
      width: clamp(34px, 2.6vw, 40px);
      height: clamp(34px, 2.6vw, 40px);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: transform 0.2s ease;
    }}

    .analytics-topic-card:hover .analytics-icon-box {{
      transform: scale(1.08);
    }}

    .analytics-card-title {{
      font-family: var(--font-display);
      font-size: clamp(0.78rem, 0.92vw, 0.98rem);
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.25;
      flex-grow: 1;
    }}

    .card-span-2 {{
      grid-column: span 2;
    }}

    .analytics-card-arrow {{
      color: #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }}

    .analytics-topic-card:hover .analytics-card-arrow {{
      color: var(--primary-red);
      transform: translateX(3px);
    }}

    .gate-modules-stack {{
      display: flex;
      flex-direction: column;
      gap: clamp(0.55rem, 1vh, 0.85rem);
      width: 100%;
    }}

    .gate-module-card {{
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 12px;
      padding: clamp(0.65rem, 1vw, 0.95rem) clamp(0.85rem, 1.2vw, 1.2rem);
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      text-align: left;
    }}

    .gate-module-card:hover {{
      border-color: var(--primary-red);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(229, 25, 36, 0.09);
    }}

    .gate-module-header {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }}

    .gate-module-title {{
      font-family: var(--font-display);
      font-size: clamp(0.88rem, 1.05vw, 1.12rem);
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.25;
    }}

    .gate-module-desc {{
      font-size: clamp(0.74rem, 0.86vw, 0.88rem);
      color: #475569;
      line-height: 1.45;
      margin: 0;
    }}

    .lifesaving-modules-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: clamp(0.45rem, 0.75vw, 0.75rem);
      width: 100%;
    }}

    .lifesaving-module-card {{
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 12px;
      padding: clamp(0.55rem, 0.8vw, 0.85rem) clamp(0.65rem, 0.95vw, 1rem);
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      text-align: left;
    }}

    .lifesaving-module-card:hover {{
      border-color: var(--primary-red);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(229, 25, 36, 0.09);
    }}

    .lifesaving-card-header {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .lifesaving-card-title {{
      font-family: var(--font-display);
      font-size: clamp(0.82rem, 0.95vw, 1.02rem);
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.25;
    }}

    .lifesaving-card-desc {{
      font-size: clamp(0.72rem, 0.82vw, 0.85rem);
      color: #475569;
      line-height: 1.42;
      margin: 0;
    }}

    .analytics-right-column {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      width: 100%;
    }}

    .analytics-image-frame {{
      position: relative;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      background: #0f172a;
    }}

    .analytics-matrix-img {{
      width: 100%;
      height: auto;
      max-height: clamp(340px, 52vh, 490px);
      object-fit: cover;
      display: block;
      transition: transform 0.3s ease;
    }}

    .analytics-matrix-img:hover {{
      transform: scale(1.02);
    }}

    /* =====================================================
       PRESTIGIOUS CLIENTS SHOWCASE LAYOUT (SINGLE SLIDE 15)
       ===================================================== */
    .slide-clients-showcase-layout {{
      width: 100%;
      max-width: 1380px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: flex-start;
      gap: clamp(0.45rem, 1.1vh, 0.85rem);
      text-align: center;
    }}

    .clients-header-block {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding-bottom: 0.1rem;
    }}

    .clients-showcase-stage {{
      flex: 1;
      min-height: 0;
      width: 100%;
      display: flex;
      flex-direction: column;
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 20px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.05), 0 2px 8px rgba(229, 25, 36, 0.03);
      padding: clamp(0.75rem, 1.5vh, 1.25rem) clamp(0.85rem, 1.8vw, 1.4rem);
      overflow: hidden;
      position: relative;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }}

    .clients-showcase-stage:hover {{
      border-color: rgba(229, 25, 36, 0.35);
      box-shadow: 0 20px 48px rgba(229, 25, 36, 0.08), 0 4px 14px rgba(0, 0, 0, 0.04);
    }}

    .clients-grid-scroll-box {{
      width: 100%;
      height: 100%;
      overflow-y: auto;
      overflow-x: hidden;
      padding-right: 4px;
      scrollbar-width: thin;
      scrollbar-color: rgba(229, 25, 36, 0.35) transparent;
    }}

    .clients-grid-scroll-box::-webkit-scrollbar {{
      width: 6px;
    }}

    .clients-grid-scroll-box::-webkit-scrollbar-track {{
      background: rgba(241, 245, 249, 0.6);
      border-radius: 9999px;
    }}

    .clients-grid-scroll-box::-webkit-scrollbar-thumb {{
      background: rgba(229, 25, 36, 0.35);
      border-radius: 9999px;
    }}

    .clients-grid-scroll-box::-webkit-scrollbar-thumb:hover {{
      background: var(--primary-red);
    }}

    .clients-alphabetical-grid {{
      display: grid;
      grid-template-columns: repeat(11, 1fr);
      gap: 8px;
      width: 100%;
      align-items: stretch;
    }}

    .client-brand-card {{
      background: #ffffff;
      border: 1.2px solid rgba(226, 232, 240, 0.95);
      border-radius: 10px;
      padding: 4px 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.02);
      transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
      aspect-ratio: 220 / 140;
      position: relative;
      cursor: pointer;
    }}

    .client-brand-card:hover {{
      border-color: var(--primary-red);
      transform: translateY(-3px) scale(1.04);
      box-shadow: 0 8px 20px rgba(229, 25, 36, 0.15), 0 2px 6px rgba(0, 0, 0, 0.04);
      z-index: 2;
    }}

    .client-brand-card img {{
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
      display: block;
      transition: transform 0.2s ease;
    }}

    /* =====================================================
       SMART SECTORS ECOSYSTEM LAYOUT (SLIDE 16)
       ===================================================== */
    .slide-sectors-ecosystem-layout {{
      width: 100%;
      max-width: 1260px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;
      gap: clamp(0.7rem, 1.8vh, 1.5rem);
      text-align: center;
    }}

    .sectors-header-block {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: clamp(0.2rem, 0.4vh, 0.4rem);
    }}

    .sectors-main-quote {{
      font-family: var(--font-heading);
      font-size: clamp(1.2rem, 1.85vw, 2.05rem);
      font-weight: 800;
      color: var(--slate-dark);
      letter-spacing: -0.02em;
      line-height: 1.28;
      margin: 0;
      max-width: 950px;
    }}

    .sectors-matrix-container {{
      display: flex;
      flex-direction: column;
      gap: clamp(0.6rem, 1.3vh, 1.1rem);
      width: 100%;
    }}

    .sectors-row-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: clamp(0.6rem, 1.2vw, 1.1rem);
      width: 100%;
    }}

    .sectors-row-5 {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: clamp(0.5rem, 1vw, 0.95rem);
      width: 100%;
    }}

    .sector-card-box {{
      background: #ffffff;
      border: 1.5px solid #e2e8f0;
      border-radius: 16px;
      padding: clamp(0.85rem, 1.6vh, 1.35rem) clamp(0.5rem, 1vw, 0.9rem);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: clamp(0.45rem, 1vh, 0.75rem);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }}

    .sector-card-box::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3.5px;
      background: #94a3b8;
      transition: all 0.3s ease;
    }}

    .sector-card-box.theme-red::before {{ background: #e51924; }}
    .sector-card-box.theme-amber::before {{ background: #f59e0b; }}
    .sector-card-box.theme-blue::before {{ background: #2563eb; }}
    .sector-card-box.theme-purple::before {{ background: #9333ea; }}
    .sector-card-box.theme-cyan::before {{ background: #0891b2; }}
    .sector-card-box.theme-emerald::before {{ background: #059669; }}
    .sector-card-box.theme-pink::before {{ background: #db2777; }}
    .sector-card-box.theme-slate::before {{ background: #475569; }}

    .sector-card-box:hover {{
      transform: translateY(-4px);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.08), 0 2px 8px rgba(229, 25, 36, 0.08);
      border-color: rgba(229, 25, 36, 0.4);
    }}

    .sector-icon-stage {{
      width: clamp(52px, 4.4vw, 68px);
      height: clamp(52px, 4.4vw, 68px);
      border-radius: 50%;
      background: #f8fafc;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.3s ease;
      color: #334155;
    }}

    .sector-card-box.theme-red .sector-icon-stage {{ background: rgba(229, 25, 36, 0.08); color: #e51924; }}
    .sector-card-box.theme-amber .sector-icon-stage {{ background: rgba(245, 158, 11, 0.09); color: #d97706; }}
    .sector-card-box.theme-blue .sector-icon-stage {{ background: rgba(37, 99, 235, 0.08); color: #2563eb; }}
    .sector-card-box.theme-purple .sector-icon-stage {{ background: rgba(147, 51, 234, 0.08); color: #9333ea; }}
    .sector-card-box.theme-cyan .sector-icon-stage {{ background: rgba(8, 145, 178, 0.08); color: #0891b2; }}
    .sector-card-box.theme-emerald .sector-icon-stage {{ background: rgba(5, 150, 105, 0.08); color: #059669; }}
    .sector-card-box.theme-pink .sector-icon-stage {{ background: rgba(219, 39, 119, 0.08); color: #db2777; }}
    .sector-card-box.theme-slate .sector-icon-stage {{ background: rgba(71, 85, 105, 0.08); color: #475569; }}

    .sector-card-box:hover .sector-icon-stage {{
      transform: scale(1.12);
    }}

    .sector-card-title {{
      font-family: var(--font-heading);
      font-size: clamp(0.78rem, 0.95vw, 1.05rem);
      font-weight: 700;
      color: var(--slate-dark);
      letter-spacing: -0.01em;
      line-height: 1.25;
      text-align: center;
    }}

    /* =====================================================
       CORE TEAM SHOWCASE LAYOUT (SLIDE 17)
       ===================================================== */
    .slide-core-team-layout {{
      width: 100%;
      max-width: 1260px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: center;
      align-items: center;
      gap: clamp(0.7rem, 1.8vh, 1.4rem);
      text-align: center;
    }}

    .core-team-header-block {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.25rem;
    }}

    .core-team-showcase-stage {{
      width: 100%;
      max-width: 1180px;
      background: #ffffff;
      border: 1.5px solid #e2e8f0;
      border-radius: 20px;
      padding: clamp(0.85rem, 1.6vw, 1.5rem);
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.05), 0 2px 8px rgba(229, 25, 36, 0.04);
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      overflow: hidden;
    }}

    .core-team-showcase-stage::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #e51924, #f59e0b, #2563eb, #e51924);
    }}

    .core-team-img-wrapper {{
      width: 100%;
      border-radius: 14px;
      overflow: hidden;
      background: #f8fafc;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: inset 0 0 0 1px rgba(0, 0, 0, 0.04);
    }}

    .core-team-photo {{
      width: 100%;
      max-height: clamp(320px, 52vh, 560px);
      object-fit: contain;
      display: block;
      transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .core-team-showcase-stage:hover .core-team-photo {{
      transform: scale(1.015);
    }}

    /* =====================================================
       GENERAL 2-COL VERTICAL TOPIC LAYOUT (SLIDES 05-07)
       ===================================================== */
    .slide-topic-layout {{
      width: 100%;
      max-width: 1140px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: clamp(0.75rem, 1.6vh, 1.4rem);
    }}

    .slide-topic-header {{
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.25rem;
    }}

    .topic-category-badge {{
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--primary-red);
      letter-spacing: 0.16em;
      background: rgba(229, 25, 36, 0.08);
      padding: 0.22rem 0.65rem;
      border-radius: 4px;
    }}

    .slide-main-heading {{
      font-family: var(--font-heading);
      font-size: clamp(1.45rem, 2.2vw, 2.3rem);
      font-weight: 800;
      color: var(--charcoal);
      letter-spacing: -0.02em;
    }}

    .slide-sub-heading {{
      font-size: clamp(0.82rem, 1vw, 1rem);
      color: #64748b;
      font-weight: 500;
      max-width: 750px;
    }}

    .slide-cards-grid-2col {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: clamp(0.65rem, 1.3vw, 1.2rem);
      width: 100%;
    }}

    .info-card-item {{
      background: #ffffff;
      border: 1px solid rgba(226, 232, 240, 0.95);
      border-radius: 14px;
      padding: clamp(0.9rem, 1.4vw, 1.35rem) clamp(1rem, 1.5vw, 1.5rem);
      display: flex;
      align-items: flex-start;
      gap: clamp(0.75rem, 1.2vw, 1.15rem);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
      transition: all 0.2s ease;
    }}

    .info-card-item:hover {{
      border-color: var(--primary-red);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(229, 25, 36, 0.08);
    }}

    .info-card-icon-circle {{
      width: clamp(38px, 3.4vw, 44px);
      height: clamp(38px, 3.4vw, 44px);
      border-radius: 10px;
      background: rgba(229, 25, 36, 0.08);
      border: 1px solid rgba(229, 25, 36, 0.2);
      color: var(--primary-red);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .info-card-body {{
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      text-align: left;
    }}

    .info-card-body strong {{
      font-family: var(--font-display);
      font-size: clamp(0.92rem, 1.1vw, 1.15rem);
      font-weight: 800;
      color: var(--charcoal);
    }}

    .info-card-body span {{
      font-size: clamp(0.78rem, 0.92vw, 0.92rem);
      color: #475569;
      line-height: 1.45;
    }}

    /* =====================================================
       CONTACT SLIDE (SLIDE 08)
       ===================================================== */
    .slide-contact-clean-layout {{
      width: 100%;
      max-width: 1060px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: clamp(0.9rem, 1.8vh, 1.6rem);
      text-align: center;
    }}

    .clean-contact-header {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      gap: 0.3rem;
    }}

    .clean-contact-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: clamp(0.85rem, 1.6vw, 1.5rem);
      width: 100%;
      margin: 0 auto;
    }}

    .clean-contact-card {{
      background: #ffffff;
      border: 1.5px solid rgba(226, 232, 240, 0.95);
      border-radius: 14px;
      padding: clamp(1rem, 1.6vw, 1.6rem) clamp(1.1rem, 1.8vw, 1.8rem);
      display: flex;
      align-items: center;
      text-align: left;
      gap: clamp(0.85rem, 1.3vw, 1.35rem);
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.04);
      text-decoration: none;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .clean-contact-card:hover {{
      border-color: var(--primary-red);
      transform: translateY(-3px);
      box-shadow: 0 12px 30px rgba(229, 25, 36, 0.1);
    }}

    .clean-contact-icon-circle {{
      width: clamp(48px, 4vw, 56px);
      height: clamp(48px, 4vw, 56px);
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .icon-circle-green {{
      background: rgba(16, 185, 129, 0.12);
      color: #10b981;
      border: 1px solid rgba(16, 185, 129, 0.28);
    }}
    .icon-circle-blue {{
      background: rgba(229, 25, 36, 0.1);
      color: var(--primary-red);
      border: 1px solid rgba(229, 25, 36, 0.28);
    }}
    .icon-circle-red {{
      background: rgba(229, 25, 36, 0.1);
      color: var(--primary-red);
      border: 1px solid rgba(229, 25, 36, 0.28);
    }}

    .clean-contact-info {{
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      min-width: 0;
    }}

    .clean-contact-label {{
      font-family: var(--font-mono);
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--slate-muted);
      letter-spacing: 0.12em;
    }}

    .clean-contact-val {{
      font-family: var(--font-display);
      font-size: clamp(1.1rem, 1.45vw, 1.55rem);
      font-weight: 800;
      color: var(--charcoal);
      line-height: 1.2;
    }}

    .clean-contact-val.hq-addr-val {{
      font-size: clamp(0.98rem, 1.25vw, 1.35rem);
    }}

    .clean-contact-sub {{
      font-size: clamp(0.72rem, 0.85vw, 0.88rem);
      color: #64748b;
      font-weight: 500;
    }}

    /* =====================================================
       3. FLOATING BOTTOM BAR
       ===================================================== */
    .floating-book-bar {{
      position: fixed;
      bottom: clamp(0.65rem, 1.4vh, 1.2rem);
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 0.45rem;
      background: rgba(16, 21, 32, 0.92);
      backdrop-filter: blur(16px);
      padding: 0.38rem 0.75rem;
      border-radius: 9999px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.28), 0 0 0 1px rgba(255, 255, 255, 0.12);
      z-index: 100;
    }}

    .nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.32rem 0.85rem;
      border-radius: 9999px;
      font-family: var(--font-display);
      font-size: 0.76rem;
      font-weight: 700;
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.15);
      background: rgba(255, 255, 255, 0.08);
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .nav-btn:hover:not(:disabled) {{
      background: rgba(255, 255, 255, 0.2);
    }}

    .nav-btn:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
    }}

    .nav-btn.btn-next {{
      background: var(--primary-red);
      border-color: var(--primary-red);
    }}

    .nav-btn.btn-next:hover:not(:disabled) {{
      background: #ff1f2d;
    }}

    .slide-counter-badge {{
      display: flex;
      align-items: center;
      gap: 0.3rem;
      padding: 0.32rem 0.65rem;
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      cursor: pointer;
    }}

    /* Drawer */
    .slide-drawer-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}

    .slide-drawer-overlay.active {{
      display: flex;
    }}

    .slide-drawer-card {{
      background: #ffffff;
      border-radius: 20px;
      width: 100%;
      max-width: 650px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      padding: 1.5rem;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.2);
      border: 1px solid #e2e8f0;
    }}

    .drawer-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 1rem;
      border-bottom: 1px solid #e2e8f0;
      margin-bottom: 1rem;
    }}

    .drawer-title {{
      font-family: var(--font-heading);
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--charcoal);
    }}

    .drawer-close-btn {{
      background: none;
      border: none;
      font-size: 1.2rem;
      cursor: pointer;
      color: #64748b;
    }}

    .drawer-grid-list {{
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      overflow-y: auto;
      max-height: calc(85vh - 120px);
    }}

    .drawer-grid-item {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 0.65rem 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.65rem;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .drawer-grid-item:hover {{
      background: #ffffff;
      border-color: var(--primary-red);
    }}

    .drawer-grid-item.current {{
      background: rgba(229, 25, 36, 0.08);
      border-color: var(--primary-red);
    }}

    .drawer-item-num {{
      font-family: var(--font-mono);
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--primary-red);
    }}

    .drawer-item-name {{
      font-family: var(--font-display);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--slate-dark);
    }}

    /* =====================================================
       COMPREHENSIVE PROFESSIONAL MOBILE & TABLET RESPONSIVE
       ===================================================== */
    @media (max-width: 1080px) {{
      .premises-topics-grid-6 {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .slide-usecases-split-layout {{
        grid-template-columns: 1fr;
        gap: 1.2rem;
      }}
      .usecases-matrix-img {{
        max-height: none;
        aspect-ratio: 1024 / 573;
        object-fit: contain;
      }}
      .clients-alphabetical-grid {{
        grid-template-columns: repeat(9, 1fr);
        gap: 7px;
      }}
    }}

    @media (max-width: 900px) {{
      html, body {{
        overflow-x: hidden !important;
        overflow-y: auto !important;
        height: auto !important;
        min-height: 100% !important;
        -webkit-overflow-scrolling: touch !important;
      }}

      .app-screen-canvas {{
        height: auto !important;
        min-height: 100dvh !important;
        overflow-x: hidden !important;
        overflow-y: visible !important;
        position: relative !important;
        display: flex !important;
        flex-direction: column !important;
      }}

      .foreground-content {{
        min-height: 100dvh !important;
        height: auto !important;
        padding: 0.35rem 0.65rem 6.5rem 0.65rem !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        align-items: stretch !important;
        overflow: visible !important;
        box-sizing: border-box !important;
        width: 100% !important;
      }}

      .slide-stage-viewport {{
        flex: 1 0 auto !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        align-items: stretch !important;
        height: auto !important;
        min-height: 0 !important;
        overflow: visible !important;
        margin: 0.25rem 0 0 0 !important;
        width: 100% !important;
      }}

      .slide-page-container {{
        height: auto !important;
        min-height: 0 !important;
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        align-items: stretch !important;
      }}

      /* 1. Top Header */
      .header-row {{
        padding: 0.15rem 0 !important;
        gap: 0.25rem !important;
        height: 38px !important;
        min-height: 38px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        flex-shrink: 0 !important;
        position: sticky !important;
        top: 0 !important;
        z-index: 50 !important;
        background: rgba(248, 250, 252, 0.94) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
      }}
      .brand-logo-block .logo-img {{
        width: 95px !important;
        max-height: 22px !important;
        object-fit: contain !important;
      }}
      .brand-tagline {{
        display: none !important;
      }}
      .portal-nav-bar {{
        display: inline-flex !important;
        padding: 0.14rem 0.22rem !important;
        gap: 0.18rem !important;
        background: rgba(255, 255, 255, 0.96) !important;
        border: 1px solid rgba(226, 232, 240, 0.95) !important;
        border-radius: 9999px !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
      }}
      .portal-nav-link {{
        font-size: 0.65rem !important;
        font-weight: 700 !important;
        padding: 0.18rem 0.42rem 0.18rem 0.22rem !important;
        gap: 0.25rem !important;
        color: #334155 !important;
        white-space: nowrap !important;
      }}
      .portal-nav-link .nav-icon-badge {{
        width: 18px !important;
        height: 18px !important;
      }}
      .portal-nav-link .nav-icon-badge svg {{
        width: 10px !important;
        height: 10px !important;
      }}
      .portal-nav-link.active {{
        background: var(--primary-red) !important;
        color: #ffffff !important;
      }}
      .btn-toc-drawer {{
        padding: 0.28rem 0.52rem !important;
        font-size: 0.68rem !important;
        border-radius: 8px !important;
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        flex-shrink: 0 !important;
      }}
      .btn-toc-drawer span {{
        display: none !important;
      }}

      /* 2. Slide 1 Manifesto (Vertically & Horizontally Centered on Mobile) */
      .slide-manifesto-layout {{
        width: 100% !important;
        max-width: 100% !important;
        min-height: calc(100dvh - 175px) !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        margin: auto 0 !important;
        padding: 0.5rem 0 !important;
      }}
      .manifesto-card-stage {{
        padding: clamp(2.4rem, 6vh, 4rem) 1.4rem !important;
        border-radius: 22px !important;
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        box-shadow: 0 14px 36px rgba(0, 0, 0, 0.06), 0 2px 8px rgba(229, 25, 36, 0.04) !important;
      }}
      .manifesto-headline-box {{
        width: 100% !important;
        text-align: center !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
      }}
      .vision-title-text {{
        font-size: clamp(1.65rem, 6.8vw, 2.2rem) !important;
        line-height: 1.2 !important;
        text-align: center !important;
        letter-spacing: -0.02em !important;
      }}
      .manifesto-accent-line {{
        margin: 1.1rem auto 0 auto !important;
        width: 80px !important;
        height: 4px !important;
      }}

      /* 3. Slide 2 Smart Premises */
      .slide-premises-full-layout {{
        height: auto !important;
        gap: 1rem !important;
      }}
      .premises-desc-lead {{
        font-size: 0.84rem;
        line-height: 1.5;
      }}
      .premises-topics-grid-6 {{
        grid-template-columns: 1fr !important;
        gap: 0.55rem;
      }}
      .premise-topic-card {{
        padding: 0.85rem 1rem;
        border-radius: 12px;
      }}
      .premise-card-icon-box {{
        width: 42px;
        height: 42px;
        border-radius: 10px;
      }}
      .premise-card-title {{
        font-size: 0.96rem;
      }}

      /* 4. Slide 3 AI Used Cases */
      .slide-usecases-split-layout {{
        grid-template-columns: 1fr !important;
        display: flex !important;
        flex-direction: column !important;
        height: auto !important;
        gap: 0.85rem !important;
        width: 100% !important;
      }}
      .usecases-left-column {{
        width: 100% !important;
        gap: 0.65rem !important;
      }}
      .usecases-header-block {{
        gap: 0.2rem !important;
      }}
      .usecases-list-grid {{
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 0.42rem 0.5rem !important;
        width: 100% !important;
      }}
      .usecase-item {{
        display: flex !important;
        align-items: center !important;
        gap: 0.45rem !important;
        padding: 0.42rem 0.55rem !important;
        border-radius: 9px !important;
        background: #ffffff !important;
        border: 1.2px solid rgba(226, 232, 240, 0.95) !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02) !important;
        min-width: 0 !important;
        box-sizing: border-box !important;
      }}
      .usecase-check-circle {{
        width: 20px !important;
        height: 20px !important;
        min-width: 20px !important;
        border-radius: 50% !important;
        background: rgba(229, 25, 36, 0.09) !important;
        color: var(--primary-red) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        flex-shrink: 0 !important;
      }}
      .usecase-check-circle svg {{
        width: 13px !important;
        height: 13px !important;
      }}
      .usecase-name {{
        font-size: 0.74rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        color: #0f172a !important;
        word-break: break-word !important;
      }}
      .usecases-right-column {{
        width: 100% !important;
        margin-top: 0.35rem !important;
      }}
      .usecases-image-frame {{
        width: 100% !important;
        border-radius: 14px !important;
        overflow: hidden !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08) !important;
        border: 1.5px solid rgba(226, 232, 240, 0.95) !important;
        background: #0f172a !important;
      }}
      .usecases-matrix-img {{
        width: 100% !important;
        max-height: none !important;
        height: auto !important;
        aspect-ratio: 1024 / 573 !important;
        object-fit: contain !important;
        display: block !important;
      }}

      /* 5. Slides 4-14 All Split Analytics & Feature Layouts */
      .slide-analytics-split-layout {{
        grid-template-columns: 1fr !important;
        display: flex !important;
        flex-direction: column !important;
        height: auto !important;
        gap: 0.95rem !important;
        width: 100% !important;
        text-align: left !important;
      }}
      .analytics-left-column {{
        width: 100% !important;
        gap: 0.65rem !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        text-align: left !important;
      }}
      .analytics-header-block {{
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        text-align: left !important;
        gap: 0.25rem !important;
      }}
      .analytics-header-block .slide-main-heading {{
        text-align: left !important;
      }}
      .analytics-desc-lead {{
        font-size: 0.78rem !important;
        line-height: 1.44 !important;
        color: #475569 !important;
        margin-top: 0.15rem !important;
        text-align: left !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
      }}
      .analytics-cards-grid {{
        grid-template-columns: 1fr !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 0.45rem !important;
        width: 100% !important;
      }}
      .card-span-2 {{
        grid-column: auto !important;
      }}
      .analytics-topic-card {{
        padding: 0.6rem 0.85rem !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        gap: 0.7rem !important;
        width: 100% !important;
        box-sizing: border-box !important;
        background: #ffffff !important;
        border: 1.5px solid rgba(226, 232, 240, 0.95) !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02) !important;
      }}
      .analytics-icon-box {{
        width: 34px !important;
        height: 34px !important;
        min-width: 34px !important;
        border-radius: 9px !important;
        flex-shrink: 0 !important;
      }}
      .analytics-card-title {{
        font-size: 0.84rem !important;
        font-weight: 700 !important;
        line-height: 1.25 !important;
        flex: 1 !important;
        color: #0f172a !important;
        margin: 0 !important;
      }}
      .analytics-card-arrow {{
        margin-left: auto !important;
        flex-shrink: 0 !important;
        color: #94a3b8 !important;
        display: flex !important;
        align-items: center !important;
      }}
      .gate-modules-stack {{
        gap: 0.55rem !important;
        width: 100% !important;
      }}
      .gate-module-card {{
        padding: 0.75rem 0.95rem !important;
        border-radius: 12px !important;
      }}
      .gate-module-title {{
        font-size: 0.92rem !important;
      }}
      .gate-module-desc {{
        font-size: 0.78rem !important;
      }}
      .lifesaving-modules-grid {{
        grid-template-columns: 1fr !important;
        gap: 0.55rem !important;
        width: 100% !important;
      }}
      .lifesaving-module-card {{
        padding: 0.75rem 0.95rem !important;
        border-radius: 12px !important;
      }}
      .lifesaving-card-title {{
        font-size: 0.88rem !important;
      }}
      .lifesaving-card-desc {{
        font-size: 0.76rem !important;
      }}
      .analytics-right-column {{
        width: 100% !important;
        margin-top: 0.35rem !important;
      }}
      .analytics-image-frame {{
        width: 100% !important;
        border-radius: 14px !important;
        overflow: hidden !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08) !important;
        border: 1.5px solid rgba(226, 232, 240, 0.95) !important;
        position: relative !important;
      }}
      .analytics-matrix-img {{
        width: 100% !important;
        max-height: 220px !important;
        height: auto !important;
        object-fit: cover !important;
        display: block !important;
      }}
      .usecases-image-overlay-badge {{
        position: absolute !important;
        bottom: 0.45rem !important;
        left: 0.45rem !important;
        right: 0.45rem !important;
        background: rgba(15, 23, 42, 0.88) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 8px !important;
        padding: 0.32rem 0.55rem !important;
        font-size: 0.62rem !important;
        color: #f8fafc !important;
        white-space: normal !important;
        display: flex !important;
        align-items: center !important;
        gap: 0.4rem !important;
      }}

      /* 6. Slide 15 Prestigious Clients (Mobile & Android Responsive) */
      .slide-clients-showcase-layout {{
        height: auto !important;
        min-height: calc(100dvh - 170px) !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
        align-items: center !important;
        gap: 0.75rem !important;
        width: 100% !important;
        padding: 0.2rem 0 1.5rem 0 !important;
      }}
      .clients-header-block {{
        width: 100% !important;
        padding-bottom: 0 !important;
      }}
      .clients-showcase-stage {{
        width: 100% !important;
        height: auto !important;
        max-height: none !important;
        padding: 0.75rem 0.5rem !important;
        border-radius: 16px !important;
        overflow: visible !important;
        border: 1.5px solid rgba(229, 25, 36, 0.22) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06), 0 2px 8px rgba(229, 25, 36, 0.04) !important;
      }}
      .clients-grid-scroll-box {{
        width: 100% !important;
        height: auto !important;
        max-height: none !important;
        overflow: visible !important;
        padding-right: 0 !important;
      }}
      .clients-alphabetical-grid {{
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 6px !important;
        width: 100% !important;
      }}
      .client-brand-card {{
        padding: 4px 5px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(226, 232, 240, 0.95) !important;
        aspect-ratio: 220 / 140 !important;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.02) !important;
      }}
      .client-brand-card:active {{
        transform: scale(0.97) !important;
        border-color: var(--primary-red) !important;
      }}
      .client-brand-card img {{
        max-width: 100% !important;
        max-height: 100% !important;
      }}

      /* 7. Slide 16 Sector Ecosystem (9 Sectors) */
      .slide-sectors-ecosystem-layout {{
        height: auto !important;
        gap: 0.9rem !important;
        width: 100% !important;
      }}
      .sectors-main-quote {{
        font-size: 1.12rem !important;
        line-height: 1.35 !important;
        padding: 0 0.25rem !important;
      }}
      .sectors-matrix-container {{
        gap: 0.55rem !important;
        width: 100% !important;
      }}
      .sectors-row-4 {{
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 0.5rem !important;
        width: 100% !important;
      }}
      .sectors-row-5 {{
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 0.5rem !important;
        width: 100% !important;
      }}
      .sectors-row-5 > :last-child {{
        grid-column: span 2 !important;
      }}
      .sector-card-box {{
        padding: 0.75rem 0.45rem !important;
        border-radius: 12px !important;
        gap: 0.35rem !important;
      }}
      .sector-icon-stage {{
        width: 44px !important;
        height: 44px !important;
      }}
      .sector-icon-stage svg {{
        width: 24px !important;
        height: 24px !important;
      }}
      .sector-card-title {{
        font-size: 0.82rem !important;
      }}

      /* 8. Slide 17 Core Team */
      .slide-core-team-layout {{
        height: auto !important;
        gap: 0.9rem !important;
        width: 100% !important;
      }}
      .core-team-showcase-stage {{
        width: 100% !important;
        padding: 0.65rem 0.45rem !important;
        border-radius: 14px !important;
      }}
      .core-team-photo {{
        width: 100% !important;
        max-height: 250px !important;
        height: auto !important;
        object-fit: contain !important;
      }}

      /* 9. Slide 18 Contact Us */
      .slide-contact-clean-layout {{
        height: auto !important;
        gap: 0.85rem !important;
        width: 100% !important;
      }}
      .clean-contact-grid {{
        grid-template-columns: 1fr !important;
        gap: 0.55rem !important;
        width: 100% !important;
      }}
      .clean-contact-card {{
        padding: 0.85rem 1rem !important;
        border-radius: 12px !important;
        gap: 0.75rem !important;
      }}
      .clean-contact-icon-circle {{
        width: 42px !important;
        height: 42px !important;
        border-radius: 10px !important;
      }}
      .clean-contact-val {{
        font-size: 1.02rem !important;
      }}
      .clean-contact-val.hq-addr-val {{
        font-size: 0.92rem !important;
      }}

      /* 10. General Titles & Badges */
      .slide-main-heading {{
        font-size: 1.35rem !important;
        line-height: 1.25 !important;
      }}
      .slide-sub-heading {{
        font-size: 0.82rem !important;
        line-height: 1.45 !important;
      }}
      .topic-category-badge {{
        font-size: 0.64rem !important;
        padding: 0.2rem 0.55rem !important;
      }}
      .slide-cards-grid-2col {{
        grid-template-columns: 1fr !important;
        gap: 0.55rem !important;
      }}

      /* 11. Floating Navigation Bar on Mobile */
      .floating-book-bar {{
        bottom: 0.6rem !important;
        width: calc(100% - 1.5rem) !important;
        max-width: 340px !important;
        padding: 0.32rem 0.65rem !important;
        gap: 0.35rem !important;
        justify-content: space-between !important;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45) !important;
        z-index: 100 !important;
      }}
      .nav-btn {{
        padding: 0.32rem 0.75rem !important;
        font-size: 0.74rem !important;
      }}
      .slide-counter-badge {{
        font-size: 0.72rem !important;
        padding: 0.22rem 0.45rem !important;
      }}

      /* 12. Slide Table of Contents Drawer on Mobile */
      .slide-drawer-card {{
        width: 92% !important;
        max-height: 85vh !important;
        padding: 1rem 0.85rem !important;
        border-radius: 16px !important;
      }}
      .drawer-grid-list {{
        max-height: calc(85vh - 75px) !important;
        gap: 0.45rem !important;
      }}
      .drawer-grid-item {{
        padding: 0.55rem 0.75rem !important;
        font-size: 0.8rem !important;
      }}
    }}

    @media (max-width: 420px) {{
      .clients-alphabetical-grid {{
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 5px !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Reading Progress Bar -->
  <div class="slide-progress-tracker">
    <div class="slide-progress-fill" id="slideProgressFill"></div>
  </div>

  <!-- Master Canvas Container -->
  <div class="app-screen-canvas is-cover-slide" id="mainCanvasContainer">
    
    <!-- Geometric Tint Shapes -->
    <div class="cover-bg-polygon-top"></div>
    <div class="cover-bg-polygon-right"></div>

    <!-- Neural Particle Canvas -->
    <canvas id="neuralCanvas"></canvas>

    <div class="foreground-content">
      <!-- 1. HEADER ROW -->
      <header class="header-row">
        <!-- Logo Block linking to index.html -->
        <a href="index.html" class="brand-logo-block" title="Back to Nimit Home">
          <img src="assets/nimit_logo_transparent.png" alt="NIMIT" class="logo-img" onerror="this.src='assets/nimit_logo.png'" />
        </a>

        <!-- Center Portal Navigation Links -->
        <nav class="portal-nav-bar">
          <a href="index.html" class="portal-nav-link" title="Return to Company Hub">
            <span class="nav-icon-badge">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
              </svg>
            </span>
            <span>Company Hub</span>
          </a>
          <a href="modules.html" class="portal-nav-link" title="Explore AI Modules Catalog">
            <span class="nav-icon-badge">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="4" y="4" width="16" height="16" rx="2"></rect>
                <rect x="9" y="9" width="6" height="6"></rect>
                <line x1="9" y1="1" x2="9" y2="4"></line>
                <line x1="15" y1="1" x2="15" y2="4"></line>
                <line x1="9" y1="20" x2="9" y2="23"></line>
                <line x1="15" y1="20" x2="15" y2="23"></line>
                <line x1="20" y1="9" x2="23" y2="9"></line>
                <line x1="20" y1="14" x2="23" y2="14"></line>
                <line x1="1" y1="9" x2="4" y2="9"></line>
                <line x1="1" y1="14" x2="4" y2="14"></line>
              </svg>
            </span>
            <span>AI Modules</span>
          </a>
        </nav>

        <!-- Right Header Tools (TOC Drawer) -->
        <div class="header-right-tools">
          <button class="btn-toc-drawer" onclick="toggleSlideDrawer()" title="View All {total_count} Slides">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
            <span>All Slides</span>
          </button>
        </div>
      </header>

      <!-- 2. DYNAMIC SLIDE VIEWPORT -->
      <main class="slide-stage-viewport" id="slideStage">
        <div class="slide-page-container" id="slideContent"></div>
      </main>

      <!-- 3. FOOTER -->
      <footer style="height:1px;"></footer>
    </div>
  </div>

  <!-- Floating Navigation Bar -->
  <div class="floating-book-bar">
    <button class="nav-btn btn-prev" id="btnPrev" onclick="prevSlide()" title="Previous Slide (←)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
      <span>Prev</span>
    </button>

    <div class="slide-counter-badge" id="slideCounterBadge" onclick="toggleSlideDrawer()" title="View Table of Contents">
      <span id="currentSlideDisplay">PAGE 01</span>
      <span style="opacity:0.4;">/</span>
      <span style="opacity:0.8;">{total_count:02d}</span>
    </div>

    <button class="nav-btn btn-next" id="btnNext" onclick="nextSlide()" title="Next Slide (→)">
      <span>Next</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
    </button>
  </div>

  <!-- Slide Index Drawer Modal -->
  <div class="slide-drawer-overlay" id="slideDrawer" onclick="closeDrawerOnBg(event)">
    <div class="slide-drawer-card">
      <div class="drawer-header">
        <span class="drawer-title">🌐 Industry Solutions — {total_count} Slides</span>
        <button class="drawer-close-btn" onclick="toggleSlideDrawer()">✕</button>
      </div>
      <div class="drawer-grid-list" id="drawerList"></div>
    </div>
  </div>

  <!-- Presentation Script -->
  <script>
    const slidesData = {slides_json_str};
    let currentSlide = 1;
    const totalSlides = slidesData.length;
    let isTransitioning = false;

    function populateDrawer() {{
      const list = document.getElementById('drawerList');
      if (!list) return;
      list.innerHTML = slidesData.map(s => `
        <div class="drawer-grid-item ${{s.num === currentSlide ? 'current' : ''}}" onclick="goToSlide(${{s.num}}); toggleSlideDrawer();">
          <span class="drawer-item-num">${{String(s.num).padStart(2, '0')}}</span>
          <span class="drawer-item-name">${{s.title}}</span>
        </div>
      `).join('');
    }}

    function toggleSlideDrawer() {{
      const drawer = document.getElementById('slideDrawer');
      if (!drawer) return;
      drawer.classList.toggle('active');
      if (drawer.classList.contains('active')) {{
        populateDrawer();
      }}
    }}

    function closeDrawerOnBg(e) {{
      if (e.target.id === 'slideDrawer') {{
        toggleSlideDrawer();
      }}
    }}

    function renderSlide(pageNum) {{
      const container = document.getElementById('slideContent');
      const canvasContainer = document.getElementById('mainCanvasContainer');
      const slide = slidesData.find(s => s.num === pageNum);
      if (!slide || !container || !canvasContainer) return;

      // Update background mode based on slide type
      if (slide.type === 'manifesto' || slide.type === 'cover') {{
        canvasContainer.className = 'app-screen-canvas is-cover-slide';
      }} else {{
        canvasContainer.className = 'app-screen-canvas is-content-slide';
      }}

      container.classList.add('fade-out');

      setTimeout(() => {{
        container.innerHTML = slide.html;
        container.classList.remove('fade-out');
        const stage = document.getElementById('slideStage');
        if (stage) stage.scrollTop = 0;
        window.scrollTo(0, 0);

        document.getElementById('currentSlideDisplay').innerText = `PAGE ${{String(pageNum).padStart(2, '0')}}`;
        document.getElementById('btnPrev').disabled = (pageNum === 1);
        document.getElementById('btnNext').disabled = (pageNum === totalSlides);

        const progress = (pageNum / totalSlides) * 100;
        document.getElementById('slideProgressFill').style.width = progress + '%';

        isTransitioning = false;
      }}, 180);
    }}

    function goToSlide(num) {{
      if (num < 1 || num > totalSlides || num === currentSlide || isTransitioning) return;
      isTransitioning = true;
      currentSlide = num;
      renderSlide(currentSlide);
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) {{
        goToSlide(currentSlide + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        goToSlide(currentSlide - 1);
      }}
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter' || e.key === 'PageDown') {{
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || e.key === 'Backspace') {{
        prevSlide();
      }} else if (e.key === 'Home') {{
        goToSlide(1);
      }} else if (e.key === 'End') {{
        goToSlide(totalSlides);
      }} else if (e.key.toLowerCase() === 'm') {{
        toggleSlideDrawer();
      }} else if (e.key === 'Escape') {{
        const drawer = document.getElementById('slideDrawer');
        if (drawer && drawer.classList.contains('active')) toggleSlideDrawer();
      }}
    }});

    // Pure Horizontal Touch Swipe Navigation for Mobile (Left / Right Only)
    // Vertical scrolling is kept 100% free & native so users can easily scroll down to see images & content
    let touchStartX = 0;
    let touchStartY = 0;

    window.addEventListener('touchstart', (e) => {{
      if (!e.changedTouches || e.changedTouches.length === 0) return;
      touchStartX = e.changedTouches[0].clientX;
      touchStartY = e.changedTouches[0].clientY;
    }}, {{ passive: true }});

    window.addEventListener('touchend', (e) => {{
      if (!e.changedTouches || e.changedTouches.length === 0) return;
      const drawer = document.getElementById('slideDrawer');
      if (drawer && drawer.classList.contains('active')) return;

      const touchEndX = e.changedTouches[0].clientX;
      const touchEndY = e.changedTouches[0].clientY;
      const diffX = touchEndX - touchStartX;
      const diffY = touchEndY - touchStartY;
      const absX = Math.abs(diffX);
      const absY = Math.abs(diffY);

      // ONLY trigger slide change on clear, intentional horizontal swipe (Left / Right)
      // Must be predominantly horizontal (absX > absY * 1.5) and exceed 50px threshold
      // Never intercept vertical scroll movements
      if (absX > 50 && absX > absY * 1.5) {{
        if (diffX < 0) {{
          nextSlide(); // Swipe Left -> Next Slide
        }} else {{
          prevSlide(); // Swipe Right -> Previous Slide
        }}
      }}
    }}, {{ passive: true }});

    window.addEventListener('DOMContentLoaded', () => {{
      renderSlide(1);
    }});

    // 60FPS Light Theme Neural Canvas Particles (Matching AI Modules)
    const canvas = document.getElementById('neuralCanvas');
    const ctx = canvas.getContext('2d');
    let width, height;
    let particles = [];
    const particleCount = 42;
    const maxDistance = 140;

    let mouse = {{ x: null, y: null, radius: 150 }};

    function resizeCanvas() {{
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class Particle {{
      constructor() {{
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.vx = (Math.random() - 0.5) * 0.7;
        this.vy = (Math.random() - 0.5) * 0.7;
        this.radius = Math.random() * 2 + 1;
        this.isRed = Math.random() < 0.25;
        this.color = this.isRed ? '#e51924' : '#94a3b8';
        this.pulse = Math.random() * Math.PI;
      }}

      update() {{
        this.x += this.vx;
        this.y += this.vy;
        this.pulse += 0.03;

        if (this.x < 0 || this.x > width) this.vx *= -1;
        if (this.y < 0 || this.y > height) this.vy *= -1;

        if (mouse.x !== null && mouse.y !== null) {{
          let dx = this.x - mouse.x;
          let dy = this.y - mouse.y;
          let dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < mouse.radius) {{
            let force = (mouse.radius - dist) / mouse.radius;
            this.x += (dx / dist) * force * 1.5;
            this.y += (dy / dist) * force * 1.5;
          }}
        }}
      }}

      draw() {{
        const pulseSize = this.radius + Math.sin(this.pulse) * 0.5;
        ctx.beginPath();
        ctx.arc(this.x, this.y, Math.max(0.5, pulseSize), 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.shadowBlur = this.isRed ? 6 : 3;
        ctx.shadowColor = this.isRed ? 'rgba(229, 25, 36, 0.5)' : 'rgba(100, 116, 139, 0.3)';
        ctx.fill();
        ctx.shadowBlur = 0;
      }}
    }}

    for (let i = 0; i < particleCount; i++) {{
      particles.push(new Particle());
    }}

    window.addEventListener('mousemove', (e) => {{
      mouse.x = e.clientX;
      mouse.y = e.clientY;
    }});

    window.addEventListener('mouseleave', () => {{
      mouse.x = null;
      mouse.y = null;
    }});

    function animate() {{
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < particles.length; i++) {{
        for (let j = i + 1; j < particles.length; j++) {{
          let dx = particles[i].x - particles[j].x;
          let dy = particles[i].y - particles[j].y;
          let dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < maxDistance) {{
            let alpha = 1 - dist / maxDistance;
            let isRedLink = particles[i].isRed || particles[j].isRed;
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.strokeStyle = isRedLink
              ? `rgba(229, 25, 36, ${{alpha * 0.35}})`
              : `rgba(148, 163, 184, ${{alpha * 0.25}})`;
            ctx.lineWidth = 1;
            ctx.stroke();
          }}
        }}
      }}

      for (let i = 0; i < particles.length; i++) {{
        particles[i].update();
        particles[i].draw();
      }}

      requestAnimationFrame(animate);
    }}
    animate();
  </script>
</body>
</html>
'''

with open(os.path.join(ROOT_DIR, 'solutions.html'), 'w', encoding='utf-8') as f:
    f.write(html_template.strip() + '\n')

print('Successfully generated solutions.html!')
