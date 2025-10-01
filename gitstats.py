import subprocess
import matplotlib.pyplot as plt
import sys

# Default number of commits to skip

X = int(sys.argv[1]) if len(sys.argv) > 1 else 50

# Get the git log with number of lines added and deleted per commit
log_output = subprocess.check_output(
    ["git", "log", "--pretty=format:%H %ad", "--date=short", "--numstat"],
    universal_newlines=True
)

# Parse the log output
commits = []
total_lines = 0
lines_changed_percent = []

for line in log_output.splitlines():
    if line.strip() == "":
        continue
    if line[0].isdigit() or line[0] == '-':
        parts = line.split()
        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
            added = int(parts[0])
            deleted = int(parts[1])
            changed = added + deleted
            if total_lines > 0:
                lines_changed_percent.append((changed / total_lines) * 100)
            else:
                lines_changed_percent.append(0)
            total_lines += added - deleted
            commits.append(total_lines)

# Filter out the first X commits
commits_filtered = commits[X:]
lines_changed_percent_filtered = lines_changed_percent[X:]
commit_indices_filtered = list(range(X, X + len(commits_filtered)))

# Create a plot with two Y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot total lines of code
ax1.set_xlabel('Commit Index (Chronological Order)')
ax1.set_ylabel('Total Lines of Code', color='tab:blue')
ax1.plot(commit_indices_filtered, commits_filtered, marker='o', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot percentage of lines changed
ax2 = ax1.twinx()
ax2.set_ylabel('Percentage of Lines Changed', color='tab:orange')
ax2.plot(commit_indices_filtered, lines_changed_percent_filtered, marker='o', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title(f'Code Evolution (Skipping First {X} Commits)')
fig.tight_layout()
plt.savefig('code_evolution_dual_axis_filtered.png')
plt.show()




#import subprocess
#import matplotlib.pyplot as plt
#
## Get the git log with number of lines added and deleted per commit
#log_output = subprocess.check_output(
#    ["git", "log", "--pretty=format:%H %ad", "--date=short", "--numstat"],
#    universal_newlines=True
#)
#
## Parse the log output
#commits = []
#total_lines = 0
#lines_changed_percent = []
#commit_hashes = []
#
#for line in log_output.splitlines():
#    if line.strip() == "":
#        continue
#    if line[0].isdigit() or line[0] == '-':
#        parts = line.split()
#        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
#            added = int(parts[0])
#            deleted = int(parts[1])
#            changed = added + deleted
#            if total_lines > 0:
#                lines_changed_percent.append((changed / total_lines) * 100)
#            else:
#                lines_changed_percent.append(0)
#            total_lines += added - deleted
#            commits.append(total_lines)
#    else:
#        commit_hash = line.split()[0]
#        commit_hashes.append(commit_hash)
#
## Ensure the lists are aligned
#commit_indices = list(range(len(commits)))
#
## Create a plot with two Y-axes
#fig, ax1 = plt.subplots(figsize=(12, 6))
#
## Plot total lines of code on the first Y-axis
#color = 'tab:blue'
#ax1.set_xlabel('Commit Index (Chronological Order)')
#ax1.set_ylabel('Total Lines of Code', color=color)
#ax1.plot(commit_indices, commits, marker='o', color=color, label='Total Lines of Code')
#ax1.tick_params(axis='y', labelcolor=color)
#
## Create a second Y-axis for percentage of lines changed
#ax2 = ax1.twinx()
#color = 'tab:orange'
#ax2.set_ylabel('Percentage of Lines Changed', color=color)
#ax2.plot(commit_indices, lines_changed_percent, marker='o', color=color, label='Percentage of Lines Changed')
#ax2.tick_params(axis='y', labelcolor=color)
#
## Add title and layout
#plt.title('Code Evolution: Total Lines vs. Percentage Changed per Commit')
#fig.tight_layout()
#plt.savefig('code_evolution_dual_axis.png')
#plt.show()





#import subprocess
#import matplotlib.pyplot as plt
#
## Get the git log with number of lines added and deleted per commit
#log_output = subprocess.check_output(
#    ["git", "log", "--pretty=format:%H %ad", "--date=short", "--numstat"],
#    universal_newlines=True
#)
#
## Parse the log output
#commits = []
#total_lines = 0
#lines_changed_percent = []
#commit_hashes = []
#
#for line in log_output.splitlines():
#    if line.strip() == "":
#        continue
#    if line[0].isdigit() or line[0] == '-':
#        parts = line.split()
#        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
#            added = int(parts[0])
#            deleted = int(parts[1])
#            changed = added + deleted
#            if total_lines > 0:
#                lines_changed_percent.append((changed / total_lines) * 100)
#            else:
#                lines_changed_percent.append(0)
#            total_lines += added - deleted
#            commits.append(total_lines)
#    else:
#        commit_hash = line.split()[0]
#        commit_hashes.append(commit_hash)
#
## Ensure the lists are aligned
#commit_indices = list(range(len(commits)))
#
## Plot total lines of code vs. commits
#plt.figure(figsize=(12, 6))
#plt.plot(commit_indices, commits, marker='o')
#plt.title('Total Lines of Code vs. Commits')
#plt.xlabel('Commit Index (Chronological Order)')
#plt.ylabel('Total Lines of Code')
#plt.grid(True)
#plt.tight_layout()
#plt.savefig('total_lines_vs_commits.png')
#
## Plot percentage of lines changed per commit
#plt.figure(figsize=(12, 6))
#plt.plot(commit_indices, lines_changed_percent, marker='o', color='orange')
#plt.title('Percentage of Lines Changed per Commit')
#plt.xlabel('Commit Index (Chronological Order)')
#plt.ylabel('Percentage of Lines Changed')
#plt.grid(True)
#plt.tight_layout()
#plt.savefig('percentage_lines_changed.png')
