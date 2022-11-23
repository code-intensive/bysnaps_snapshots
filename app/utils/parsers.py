def public_id_from_snap_url(snap_url: str, prefix: str = "buysnaps/snap-shots") -> str:
    """Parses a cloudinary public id from the public url.

    :param snap_url: The snap_url from which to retrieve the public_id.

    :param prefix: An optional prefix to be prepended to the snap_url.

    :return: Snap public URL.

    :rtype: str.
    """
    # The cloudinary image below is a perfect
    # example of what we intend to parse as the
    # value with a png extension is what we intend
    # to retrieve without the extension,
    # that is the public_id of the particular resource

    # http://res.cloudinary.com/djciset6u/image/upload/v1667867432/buysnaps/snap-shots/w9kjdjuknebppord0nm1.png # noqa

    cloudinary_resource = snap_url.split("/")[-1]  # w9kjdjuknebppord0nm1.png

    # To be on the safe side, we perform an extra split using "."
    # incase the resource has a different file extension.
    # finally, the provided prefix is prepended to
    # the public_id to make it whole, i.e
    # buysnaps/snap-shots/w9kjdjuknebppord0nm1
    return prefix + "/" + cloudinary_resource.split(".")[0]
