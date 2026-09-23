# -*- coding: utf-8 -*-
"""
Script to update all 11 AI Module introductory description paragraphs in builders/build_catalog.py
to natural, professional, human-written phrasing without repetitive 'CCTV analytics...' prefixes.
"""

REPLACEMENTS = {
    # Module 01
    """                <p class="analytics-desc-lead">
                  Computer vision monitors workers through existing CCTV cameras and detects whether required safety equipment is being worn in real time. It helps identify PPE violations quickly and supports faster action to maintain workplace safety.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Continuous safety monitoring automatically checks workers across active zones for required helmets, vests, and protective gear, dispatching instant notifications to safety officers.
                </p>""",

    # Module 02
    """                <p class="analytics-desc-lead">
                  ANPR systems use CCTV and OCR technology to detect and read vehicle number plates in real time. It helps automate gate access, improve security, and identify restricted vehicles.
                </p>""":
    """                <p class="analytics-desc-lead">
                  High-accuracy license plate recognition captures vehicle numbers in real time at entry and exit gates to automate boom barriers and record complete access audit logs.
                </p>""",

    # Module 03
    """                <p class="analytics-desc-lead">
                  Smart camera systems use existing CCTV cameras to detect fire and smoke in real time. They identify visual signs of danger and send early alerts, helping teams respond quickly and reduce the risk of serious damage.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Early hazard detection identifies visual flame and smoke patterns in real time, delivering instant alarms to plant response teams to mitigate critical fire risks.
                </p>""",

    # Module 04
    """                <p class="analytics-desc-lead">
                  CCTV analytics track vehicle movement, estimate speed, and identify speeding violations in real time. It records details such as number plates and time to support safer roads and faster action.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Real-time velocity tracking monitors campus and highway traffic to identify speeding violations instantly with timestamped vehicle plate logs.
                </p>""",

    # Module 05
    """                <p class="analytics-desc-lead">
                  Computer vision detects and counts products moving through factory conveyors in real time. It helps reduce manual counting errors, track production, and improve inventory management.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Automated optical tracking counts and categorizes products moving along factory assembly lines, eliminating manual counting errors and providing live inventory metrics.
                </p>""",

    # Module 06
    """                <p class="analytics-desc-lead">
                  CCTV analytics detect and track people to count entries and exits in real time. It helps monitor footfall, understand movement patterns, and manage occupancy across different areas.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Bi-directional footfall tracking measures visitor entries and exits in real time, providing accurate occupancy numbers, flow patterns, and density heatmaps.
                </p>""",

    # Module 07
    """                <p class="analytics-desc-lead">
                  Face recognition detects faces and matches them with registered profiles in real time. It helps enable secure, touchless access and identify authorized or restricted individuals.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Contactless biometric recognition matches faces against authorized employee profiles in milliseconds, enabling seamless entry and immediate blacklist alerts.
                </p>""",

    # Module 08
    """                <p class="analytics-desc-lead">
                  Smart cameras detect people, vehicles, and obstacles near moving forklifts. When someone or something enters a defined safety zone, the system alerts the operator to help prevent collisions.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Proximity hazard detection monitors moving forklift blindspots in real time, triggering instant operator cab alarms to prevent warehouse collisions.
                </p>""",

    # Module 09
    """                <p class="analytics-desc-lead">
                  CCTV analytics detect falls and sudden changes in posture using body movement and pose tracking. It sends real-time alerts to staff, helping them respond quickly and improve worker safety.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Human pose estimation detects slips, trips, and sudden posture collapse in real time, alerting floor supervisors and safety personnel for rapid emergency response.
                </p>""",

    # Module 10
    """                <p class="analytics-desc-lead">
                  CCTV analytics monitor fences, walls, and virtual boundaries to detect unauthorized entry by people or vehicles. It turns regular surveillance into an active security system with real-time intrusion alerts.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Virtual boundary surveillance monitors fence lines, perimeter walls, and sterile zones in real time, delivering instant alarms to prevent unauthorized human and vehicle intrusions.
                </p>""",

    # Module 11
    """                <p class="analytics-desc-lead">
                  CCTV analytics detect large animals near highways, industrial areas, and forest boundaries. It sends early alerts to help prevent accidents, protect people, and support wildlife conservation.
                </p>""":
    """                <p class="analytics-desc-lead">
                  Wildlife telemetry detects large animals approaching roadways, industrial corridors, and forest perimeters, dispatching early alerts to prevent collisions and ensure public safety.
                </p>"""
}

target_file = r"c:\nimit\builders\build_catalog.py"
with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

count = 0
for old, new in REPLACEMENTS.items():
    if old in content:
        content = content.replace(old, new)
        count += 1
    else:
        print("[-] Pattern not matched for a module")

with open(target_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"[+] Successfully replaced {count}/11 module descriptions with human-written phrasing.")
