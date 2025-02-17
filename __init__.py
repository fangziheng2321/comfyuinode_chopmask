from .cus_chopmask import chopmask
NODE_CLASS_MAPPINGS = {
    "cus_chopmask": chopmask,
}
 
NODE_DISPLAY_NAME_MAPPINGS = {
    "cus_chopmask": "custom_chopmask",
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']