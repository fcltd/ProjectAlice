VERSION = '1.0.0-b1'

DEFAULT = 'default'
UNKNOWN_WORD = 'unknownword'
UNKNOWN_USER = 'unknownUser'
UNKNOWN_MANAGER = 'unknownManager'
UNKNOWN = 'unknown'
EVERYWHERE = 'everywhere'
ALL = 'all'
RANDOM = 'random'
DUMMY = 'dummy'
DATABASE_FILE = 'system/database/data.db'
SKILL_INSTALL_TICKET_PATH = 'system/skillInstallTickets'
GITHUB_URL = 'https://github.com/project-alice-assistant'
GITHUB_RAW_URL = 'https://raw.githubusercontent.com/project-alice-assistant'
GITHUB_API_URL = 'https://api.github.com/repos/project-alice-assistant'
GITHUB_REPOSITORY_ID = 193512918

TOPIC_AUDIO_FRAME = 'hermes/audioServer/{}/audioFrame'
TOPIC_HOTWORD_DETECTED = 'hermes/hotword/default/detected'
TOPIC_WAKEWORD_DETECTED = 'hermes/hotword/{}/detected'
TOPIC_ASR_START_LISTENING = 'hermes/asr/startListening'
TOPIC_ASR_STOP_LISTENING = 'hermes/asr/stopListening'
TOPIC_ASR_TOGGLE_ON = 'hermes/asr/toggleOn'
TOPIC_ASR_TOGGLE_OFF = 'hermes/asr/toggleOff'
TOPIC_SESSION_STARTED = 'hermes/dialogueManager/sessionStarted'
TOPIC_SESSION_QUEUED = 'hermes/dialogueManager/sessionQueued'
TOPIC_SESSION_ENDED = 'hermes/dialogueManager/sessionEnded'
TOPIC_TEXT_CAPTURED = 'hermes/asr/textCaptured'
TOPIC_PARTIAL_TEXT_CAPTURED = 'hermes/asr/partialTextCaptured'
TOPIC_INTENT_NOT_RECOGNIZED = 'hermes/dialogueManager/intentNotRecognized'
TOPIC_NLU_INTENT_NOT_RECOGNIZED = 'hermes/nlu/intentNotRecognized'
TOPIC_NLU_ERROR = 'hermes/error/nlu'
TOPIC_INTENT_PARSED = 'hermes/nlu/intentParsed'
TOPIC_TTS_SAY = 'hermes/tts/say'
TOPIC_TTS_FINISHED = 'hermes/tts/sayFinished'
TOPIC_HOTWORD_TOGGLE_ON = 'hermes/hotword/toggleOn'
TOPIC_HOTWORD_TOGGLE_OFF = 'hermes/hotword/toggleOff'
TOPIC_PLAY_BYTES = 'hermes/audioServer/{}/playBytes/#'
TOPIC_PLAY_BYTES_FINISHED = 'hermes/audioServer/{}/playFinished'
TOPIC_START_SESSION = 'hermes/dialogueManager/startSession'
TOPIC_CONTINUE_SESSION = 'hermes/dialogueManager/continueSession'
TOPIC_END_SESSION = 'hermes/dialogueManager/endSession'
TOPIC_DIALOGUE_MANAGER_CONFIGURE = 'hermes/dialogueManager/configure'
TOPIC_TOGGLE_FEEDBACK_ON = 'hermes/feedback/sound/toggleOn'
TOPIC_TOGGLE_FEEDBACK_OFF = 'hermes/feedback/sound/toggleOff'
TOPIC_TOGGLE_FEEDBACK = 'hermes/feedback/sound/toggle{}'
TOPIC_NLU_QUERY = 'hermes/nlu/query'
TOPIC_VAD_UP = 'hermes/voiceActivity/{}/vadUp'
TOPIC_VAD_DOWN = 'hermes/voiceActivity/{}/vadDown'

TOPIC_SYSLOG = 'projectalice/logging/syslog'
TOPIC_NLU_TRAINING_STATUS = 'projectalice/nlu/trainingStatus'
TOPIC_NEW_HOTWORD = 'projectalice/devices/alice/newHotword'
TOPIC_DEVICE_HEARTBEAT = 'projectalice/devices/heartbeat'
TOPIC_CORE_HEARTBEAT = 'projectalice/devices/coreHeartbeat'
TOPIC_DND = 'projectalice/devices/stopListen'
TOPIC_STOP_DND = 'projectalice/devices/startListen'
TOPIC_TOGGLE_DND = 'projectalice/devices/toggleListen'

TOPIC_DEVICE_STATUS = 'projectalice/devices/status'
TOPIC_DEVICE_UPDATED = 'projectalice/devices/updated'

EVENT_FULL_MINUTE = 'fullMinute'
EVENT_FIVE_MINUTE = 'fiveMinute'
EVENT_QUARTER_HOUR = 'quarterHour'
EVENT_FULL_HOUR = 'fullHour'
EVENT_SKILL_UPDATED = 'skillUpdated'
EVENT_SKILL_INSTALLED = 'skillInstalled'
EVENT_BOOTED = 'booted'
EVENT_SKILL_INSTALL_FAILED = 'skillInstallFailed'
EVENT_SKILL_DELETED = 'skillDeleted'
EVENT_DEVICE_ADDED = 'deviceAdded'
EVENT_DEVICE_DISCOVERED = 'deviceDiscovered'
EVENT_DEVICE_REMOVED = 'deviceRemoved'
EVENT_DEVICE_CONNECTING = 'deviceConnecting'
EVENT_DEVICE_DISCONNECTING = 'deviceDisconnecting'
EVENT_AUDIO_FRAME = 'audioFrame'
EVENT_HOTWORD_TOGGLE_ON = 'hotwordToggleOn'
EVENT_HOTWORD_TOGGLE_OFF = 'hotwordToggleOff'
EVENT_MESSAGE = 'message'
EVENT_HOTWORD = 'hotword'
EVENT_WAKEWORD = 'wakeword'
EVENT_SESSION_STARTED = 'sessionStarted'
EVENT_SESSION_QUEUED = 'sessionQueued'
EVENT_START_LISTENING = 'startListening'
EVENT_START_SESSION = 'startSession'
EVENT_STOP_LISTENING = 'stopListening'
EVENT_ASR_TOGGLE_ON = 'asrToggleOn'
EVENT_ASR_TOGGLE_OFF = 'asrToggleOff'
EVENT_CAPTURED = 'captured'
EVENT_PARTIAL_TEXT_CAPTURED = 'partialTextCaptured'
EVENT_NLU_QUERY = 'nluQuery'
EVENT_INTENT_PARSED = 'intentParsed'
EVENT_CONTINUE_SESSION = 'continueSession'
EVENT_END_SESSION = 'endSession'
EVENT_SESSION_ENDED = 'sessionEnded'
EVENT_USER_CANCEL = 'userCancel'
EVENT_SESSION_TIMEOUT = 'sessionTimeout'
EVENT_SESSION_ERROR = 'sessionError'
EVENT_SAY = 'say'
EVENT_SAY_FINISHED = 'sayFinished'
EVENT_INTENT = 'intent'
EVENT_INTENT_NOT_RECOGNIZED = 'intentNotRecognized'
EVENT_NLU_INTENT_NOT_RECOGNIZED = 'nluIntentNotRecognized'
EVENT_SNIPS_ASSISTANT_DOWNLOAD_FAILED = 'snipsAssistantDownloadFailed'
EVENT_SNIPS_ASSISTANT_INSTALLED = 'snipsAssistantInstalled'
EVENT_SNIPS_ASSISTANT_INSTALL_FAILED = 'snipsAssistantFailedInstalling'
EVENT_INTERNET_LOST = 'internetLost'
EVENT_INTERNET_CONNECTED = 'internetConnected'
EVENT_BROADCASTING_FOR_NEW_DEVICE = 'broadcastingForNewDeviceStart'
EVENT_STOP_BROADCASTING_FOR_NEW_DEVICE = 'broadcastingForNewDeviceStop'
EVENT_WAKEUP = 'wakeup'
EVENT_SLEEP = 'sleep'
EVENT_NLU_TRAINED = 'nluTrained'
EVENT_VAD_UP = 'vadUp'
EVENT_VAD_DOWN = 'vadDown'
EVENT_CONTEXT_SENSITIVE_DELETE = 'contextSensitiveDelete'
EVENT_CONTEXT_SENSITIVE_EDIT = 'contextSensitiveEdit'
EVENT_DEVICE_HEARTBEAT = 'deviceHeartbeat'
EVENT_SYSLOG = 'sysLog'
EVENT_CONFIGURE_INTENT = 'configureIntent'
EVENT_PLAY_BYTES = 'playBytes'
EVENT_PLAY_BYTES_FINISHED = 'playBytesFinished'
EVENT_TOGGLE_FEEDBACK_ON = 'toggleFeedbackOn'
EVENT_TOGGLE_FEEDBACK_OFF = 'toggleFeedbackOff'
EVENT_NLU_ERROR = 'nluError'
EVENT_SKILL_STARTED = 'skillStarted'
EVENT_SKILL_STOPPED = 'skillStopped'
