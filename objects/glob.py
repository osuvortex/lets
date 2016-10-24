import personalBestCache
import userStatsCache
from common.ddog import datadogClient
from common.files import fileBuffer, fileLocks
from common.web import schiavo

try:
	with open("version") as f:
		VERSION = f.read()
except:
	VERSION = "¯\_(xd)_/¯"

DATADOG_PREFIX = "lets"
db = None
conf = None
application = None
pool = None

busyThreads = 0
debug = False
sentry = False

# Cache and objects
fLocks = fileLocks.fileLocks()
userIDCache = {}
userStatsCache = userStatsCache.userStatsCache()
personalBestCache = personalBestCache.personalBestCache()
fileBuffers = fileBuffer.buffersList()
dog = datadogClient.datadogClient()
schiavo = schiavo.schiavo()