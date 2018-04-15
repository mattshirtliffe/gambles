import requests

class Gambles():

    def __init__(self, url='http://localhost:8098'):
        self.url = url

    # List Buckets
    def get_buckets(self,bucket_type=None):
        """Return a list of buckets by type of no type"""
        if bucket_type:
            response = requests.get(self.url + '/types/'+ bucket_type +'/buckets', params={"buckets": "true"})
        else:
            response = requests.get(self.url+'/buckets',params={"buckets":"true"})

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return "Not Found"
        else:
            return response.status_code,response.text


    # List Keys (Should not be used in production)
    def list_key(self,bucket,bucket_type=None):

        # TODO add option to stream {"key":"stream"}
        if bucket_type:
            response = requests.get(self.url+'/types/'+ bucket_type +'/buckets/'+ bucket +'/keys', params={"keys":"true"})
        else:
            response = requests.get(self.url+'/buckets/'+ bucket +'/keys', params={"keys":"true"})

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code,response.text

    # Get Bucket Properties
    def get_bucket_properties(self,bucket, bucket_type=None):
        """Return properties of a bucket"""
        if bucket_type:
            response = requests.get(self.url+'/types/' + bucket_type + '/buckets/'+ bucket +'/props')
        else:
            response = requests.get(self.url+'/buckets/' + bucket + '/props')

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code,response.text

    # Set Bucket Properties
    def set_bucket_properties(self,bucket,data):
        """Set properties of a bucket"""
        response = requests.put(self.url + '/buckets/' + bucket + '/props', json=data)
        if response.status_code == 204:
            return None
        elif response.status_code == 404:
            return "Not Found"
        else:
            return response.status_code, response.text

    # Reset Bucket Properties
    def reset_bucket_properties(self,bucket):
        """Reset bucket properties n_val and allow_mult back to the default settings."""
        response = requests.delete(self.url+'/buckets/'+ bucket +'/props')
        if response.status_code == 204:
            return None
        elif response.status_code == 404:
            return "Not Found"
        else:
            return response.status_code,response.text

    # Server Related Operations
    def ping(self):
        response = requests.get(self.url + '/ping')
        return response

    def stats(self):
        response = requests.get(self.url + '/stats')
        return response.json()


    def resources(self):
        response = requests.get(self.url + '/')
        # return html list
        # what should be do with this?
        return response.text

    # Object Related Operations
    def fetch_object(self,bucket,type = None,key = None):
        """Reads an object from the specified bucket/key."""
        return None

    def get_object(self,bucket,type = None,key = None):
        """Reads an object from the specified bucket/key."""
        self.fetch_object(self, bucket, type, key)

    def store_object(self, bucket, type=None, key=None):
        """Stores an object under the specified bucket / key."""
        return None

    def update_object(self, bucket, type=None, key=None):
        """Stores an object under the specified bucket / key."""
        return None

    def delete_object(self, bucket, type=None, key=None):
        """delete an object under the specified bucket / key."""
        return None