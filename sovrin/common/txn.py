

TXN_TYPE = 'type'
# TODO: Should probably be a called TARGET
TARGET_NYM = 'dest'
ORIGIN = 'origin'
ROLE = 'role'
DATA = 'data'
NONCE = 'nonce'

TXN_ID = 'txnId'
SKEY = "secretKey"

allOpKeys = [TXN_TYPE, TARGET_NYM, ORIGIN, ROLE, DATA]

# client transaction types
ADD_NYM = "ADD_NYM"
ADD_ATTR = "ADD_ATTR"
IDPROOF = "IDPROOF"
ASSIGN_AGENT = "ASSIGN_AGENT"
ADD_SPONSOR = "ADD_SPONSOR"
ADD_AGENT = "ADD_AGENT"
DISCLOSE = "DISCLOSE"


# TXN_TYPE -> (requireds, optionals)
fields = {ADD_NYM: ([TARGET_NYM],        [ROLE]),
          ADD_ATTR: ([TARGET_NYM, DATA], [])
          }

validTxnTypes = [ADD_NYM,
                 ADD_ATTR,
                 IDPROOF,
                 ASSIGN_AGENT]


# def txn(txnType,
#         targetNym,
#         origin=None,
#         data=None,
#         role=None):
#     return {
#         TXN_TYPE: txnType,
#         TARGET_NYM: targetNym,
#         ORIGIN: origin,
#         DATA: data,
#         ROLE: role
#     }


def AddNym(target, role=None, origin=None):
    return newTxn(txnType=ADD_NYM, origin=origin, target=target, role=role)


# TODO: Change name to txn or some thing else after discussion
def newTxn(txnType, origin=None, target=None, data=None, role=None):
    txn = {
        TXN_TYPE: txnType
    }
    if origin:
        txn[ORIGIN] = origin
    if target:
        txn[TARGET_NYM] = target
    if data:
        txn[DATA] = data
    if role:
        txn[ROLE] = role
    return txn

# TODO: Move them to a separate file
# ROLE types
STEWARD = "STEWARD"
SPONSOR = "SPONSOR"
USER = "USER"


def storedTxn(txnTyp, dest, txnId, role=None, data=None):
    return {
        TXN_TYPE: txnTyp,
        TARGET_NYM: dest,
        TXN_ID: txnId,
        ROLE: role,
        DATA: data
    }


def getGenesisTxns():
    return [storedTxn(
        ADD_NYM,
        "aXMgYSBwaXQgYSBzZWVkLCBvciBzb21lcGluIGVsc2U=",
        "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
        role=STEWARD)
    ]