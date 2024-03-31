from django.utils.translation import gettext_lazy as _

""" Success message codes: Range [2000 - 2999] """
SUCCESS_SYNC_DISCOUNT = 2000

SUCCESS_MESSAGE_CODES = {

}

""" Error message codes: Range [4000 - 4999] """
ERROR_UNKNOWN = 4000


ERROR_MESSAGE_CODES = {
    # ERROR_CREDENTIAL_DOES_NOT_EXIST: _("Credential does not exist."),


}

""" All message codes are merged together in this section """
MESSAGE_CODES = {**SUCCESS_MESSAGE_CODES, **ERROR_MESSAGE_CODES}
