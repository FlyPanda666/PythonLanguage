import logging
from utils.common import init_logger

init_logger()
logger = logging.getLogger(__name__)

args = {
    "mode": "test",
    "max_seq_len": 300,
    "model_name_or_path": "bert-base-uncased",
    "task": "xml"
}

logger.info(args)

cached_file_path = "cached_{}_{}_{}_{}".format(
            args.get("mode"),
            args.get("task"),
            list(filter(None, args.get("model_name_or_path").split("/"))).pop(),
            args.get("max_seq_len"),
        )
logger.info(cached_file_path)

logger.info(args.get("model_name_or_path").split("/").pop())

tmp = "/Users/admin/Desktop/LanguagePython"
logger.info(tmp.split("/"))
logger.info(list(filter(None, tmp.split("/"))))


def greater_len(x):
    if len(x) > 8:
        return x
    return None


logger.info(list(filter(greater_len, tmp.split("/"))))
